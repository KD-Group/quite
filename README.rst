quite: QT UI Extension
======================

A simple extension for PySide.

I hope it is useful for you, too. :D


====================
Powerful Signal-Slot
====================

.. code-block:: python

    import quite

    signal = quite.SignalSender()
    executed = [False]

    def slot(a: int, b: int, c: int):
        self.assertEqual(a, 1)
        self.assertEqual(b, 2)
        self.assertEqual(c, 3)
        executed[0] = True
    signal.connect(slot)

    signal.emit(1, 2, 3)
    self.assertTrue(executed[0])
