package com.zer0rez.euler

object Util {
    fun swapin(target: IntArray, arrow: Int): Int {
        target[0] = target[1]
        target[1] = arrow
        return target[1]
    }

    fun fibonacci(quit: (Int) -> Boolean): ArrayList<Int> {
        var values = ArrayList<Int>()
        values.add(1)
        values.add(2)
        while (!quit(values.last())) {
            values.add(values[values.count() - 1] + values[values.count() - 2])
        }
        values.remove(values.last())
        return values
    }
}