package com.zer0rez.euler.util

import kotlin.math.sqrt

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

    fun factorize(term: Long) = sequence {
        var target = term
        var current = sqrt(target.toDouble()).toLong()
        while (current % 2 == 0L) {
            current /= 2
        }
        while (current < target) {
            print(" $current::$target")
            if (target % current == 0L) {
                yield(current)
                target = (target / current).toLong()
            }
            current -= 2
        }
    }

}