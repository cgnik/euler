
import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution
import javafx.collections.ObservableList
import javafx.geometry.Pos
import javafx.scene.layout.Priority
import org.reflections.Reflections
import tornadofx.*
import java.io.PrintStream

class ProblemApp : App(ProblemView::class)


class ProblemView : View() {

    lateinit var out: PrintStream

    val controller: Problems by inject()

    override val root = vbox {
        label("Project Euler Calculator")
        button("Begin Calculation") {
            vboxConstraints { alignment = Pos.CENTER }
            action { controller.solve() }
        }
        tableview(controller.solutions) {
            vboxConstraints { vGrow = Priority.ALWAYS }
            readonlyColumn("Problem",Solution::number)
            readonlyColumn("Answer",Solution::answer)
            readonlyColumn("Extra Info",Solution::extra)
        }
    }
}

class Problems : Controller() {
    var solutions: ObservableList<Solution> = ArrayList<Solution>().observable()
    fun solve() {
        val problems = Reflections(Problem::class.java.`package`.name).getSubTypesOf(Problem::class.java).sortedBy { it.name }
        problems.forEach { solutions.add(it.newInstance().solve()) }
    }
}

fun main(args: Array<String>) {
    launch<ProblemApp>(args)
}
