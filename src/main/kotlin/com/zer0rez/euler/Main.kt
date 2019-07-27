
import com.zer0rez.euler.Problem
import com.zer0rez.euler.Problem1
import com.zer0rez.euler.Problem2
import com.zer0rez.euler.TextAreaOutputStream
import tornadofx.*
import java.io.PrintStream

class ProblemApp : App(ProblemView::class)


class ProblemView : View() {

    lateinit var out: PrintStream

    val controller: Problems by inject()

    override val root = vbox {
        label("Project Euler Calculator")
        button("Begin Calculation") {
            action {
                controller.solve(out)
            }
        }
        textarea {
            out = PrintStream(TextAreaOutputStream(this))
        }
    }

}

class Problems : Controller(), Problem {
    val problems = arrayOf(Problem1::class.java, Problem2::class.java)

    override fun solve(out: PrintStream) {
        problems.forEach { it.newInstance().solve(out) }
    }
}

fun main(args: Array<String>) {
    launch<ProblemApp>(args)
}
