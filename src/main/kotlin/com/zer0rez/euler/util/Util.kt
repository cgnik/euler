package com.zer0rez.euler.util

import kotlin.math.sqrt

fun Int.isDivisibleBy(i: Int): Boolean = this % i == 0
fun Int.isDivisibleByAll(i: IntArray): Boolean = i.all { this.isDivisibleBy(it) }

fun Long.isDivisibleBy(i: Long): Boolean = this % i == 0L
fun Long.isDivisibleByAny(i: Collection<Long>): Boolean = i.any { this.isDivisibleBy(it) }

fun Int.isPalindrome(): Boolean {
    if (this < 10) return false;
    val ns = this.toString()
    val end = ns.length - 1
    for (i in 0..(ns.length / 2)) {
        if (i >= end) break
        if (ns[i] != ns[end - i]) return false
    }
    return true
}

fun IntArray.swapin(arrow: Int): Int {
    this[0] = this[1]
    this[1] = arrow
    return this[1]
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

fun Long.factorize(): Sequence<Long> {
    var target = this
    var current = sqrt(target.toDouble()).toLong()
    return sequence {
        while (current % 2 == 0L) current /= 2
        while (current > 0 && current < target) {
            if (target % current == 0L) {
                yield(current)
                target /= current
            }
            current -= 2
        }
    }
}

fun IntArray.productSeries(size: Int): List<Pair<Int, List<Int>>> = IntRange(0, this.count() - size).map { i ->
    Pair(this.slice(i until i + size).reduce { t, x -> x * t }, this.slice(i until i + size))
}
