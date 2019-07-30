package com.zer0rez.euler.util

import kotlin.math.sqrt

object Util {

    fun isPalindrome(num: Long): Boolean {
        if (num < 10) return false;
        val ns = num.toString()
        val end = ns.length - 1
        for (i in 0..(ns.length / 2)) {
            println("$i : $ns, /2 ${end - i}, end: $end, ")
            if (i >= end) break
            if (ns[i] != ns[end - i]) return false
        }
        return true
    }

    fun swapin(target: IntArray, arrow: Int): Int {
        target[0] = target[1]
        target[1] = arrow
        return target[1]
    }

    fun fibonacci(quit: (Int) -> Boolean): IntArray {
        var values = ArrayList<Int>()
        values.add(1)
        values.add(1)
        while (!quit(values.last())) {
            values.add(values[values.count() - 1] + values[values.count() - 2])
        }
        values.remove(values.last())
        return values.toIntArray()
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
