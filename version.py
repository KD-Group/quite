# 获取git的tag并保存在RELEASE-VERSION中, 以便每次打包自动识别最新的tag,
# 并且作为version去发布, 如果不存在RELEASE-VERSION文件且无tag, 默认使用"0.0.1"
# 使用前必须在MANIFEST.in中加入
#   include RELEASE-VERSION
#   include version.py

__all__ = ("get_git_version")

import subprocess
import os


def get_git_latest_tag():
    def _minimal_ext_cmd(cmd: str):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd("git describe --abbrev=0 --tags")
        git_tag = out.strip().decode('ascii')
        # 去除tag中的v/V
        if str(git_tag).startswith("v") or str(git_tag).startswith("V"):
            git_tag = str(git_tag)[1:]
        if git_tag == "":
            git_tag = None
    except Exception:
        git_tag = None

    return git_tag


def read_release_version():
    try:
        f = open("RELEASE-VERSION", "r")

        try:
            version = f.readlines()[0].strip()
            if version == "":
                return None
            else:
                return version
        finally:
            f.close()
    except Exception:
        return None


def write_release_version(version):
    f = open("RELEASE-VERSION", "w")
    f.write("%s\n" % version)
    f.close()


def get_git_version():
    release_version = read_release_version()
    version = get_git_latest_tag()
    if version is None:
        version = release_version

    # 如果release-version文件没有, 且git没有打tag, 则默认使用"0.0.1"
    if version is None:
        version = "0.0.1"
        # raise ValueError("Cannot find the version number!")

    if version != release_version:
        write_release_version(version)
    return version


if __name__ == "__main__":
    print(get_git_version())
