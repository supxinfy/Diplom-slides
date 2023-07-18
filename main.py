from manim import *

from manim_slides import Slide

import macwilliams as mw

class Slides(Slide):
    def construct(self):

        slide_counter = [Text(f'{i}/18').to_corner(DR) for i in range(1, 19)]
        counter = 0
        # Slide 1
        title_shit = VGroup(
            Text("Выпускная квалификационная работа бакалавра"),
            Text("Направление \"01.03.01 Математика\"")).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.5).shift(2*UP+3*LEFT)
        title_talk = VGroup(
            Text("Многочлены Бернштейна и преобразование Мак-Вильямс"),
                ).arrange(DOWN).scale(0.75)
        authors = VGroup(
            Text("19 июня 2023").scale(1.5),
            Text("студент группы 22401 Шубин В.В."),
            Text("научный руководитель: к. ф.-м. н. Гогин Н. Д.")
                ).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.4).to_corner(DL)
        self.play(FadeIn(title_shit, title_talk, authors))

        self.play(FadeIn(slide_counter[counter]))
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1

        # Slide 2
        self.play(FadeOut(title_talk, title_shit, authors))
        title1 = Title("Цели и задачи.")

        goals = VGroup(
            Tex("1. Ввести необходимые определения.", tex_environment = 'flushleft'),
            Tex("2. Предложить новый подход к вычислению многочленов Бернштейна и дать ему обоснование.", tex_environment = 'flushleft'),
            Tex("3. Исследовать возможность его приложения к вычислению многочленов Чебышева.", tex_environment = 'flushleft'),
            Tex("4. Реализовать предложенный метод в системах компьютерной алгебры Wolfram Mathematica и SageMath.", tex_environment = 'flushleft'),
            Tex("5. Представить возможные направления применения предложенного метода в других областях.", tex_environment = 'flushleft')
        ).arrange(DOWN, center = False, aligned_edge=LEFT).shift(4*LEFT + 3*UP).scale(0.6)

        self.play(FadeIn(title1, goals))

        self.play(FadeIn(slide_counter[counter]))
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1
        
        # Slide 3
        self.play(FadeOut(title1), FadeOut(goals))

        title2 = Title("Основные определения")

        title = Text(r"Определение 1.", weight=BOLD).to_corner(UL).shift(1.15 * DOWN + 0.25 * RIGHT)
        defBern = VGroup(
            Tex(r"Пусть \(f(x) \in C[0,\, 1]\). Многочлен \(B_n (f;\, x)\) степени \(n\) для вектора отсчетов \((f(0),\, f(1/n), \, \dots,\, f(1))\) определяется как многочлен", tex_environment='flushleft').scale(0.7),
            MathTex(r"B_n(f; \, x) = \sum_{r=0}^{n} \binom{n}{r} f_r x^r (1-x)^{n-r},"),
            Tex(r"где \(f_r = f(\frac{r}{n})\).", tex_environment='flushleft')
        ).arrange(DOWN, center=False, aligned_edge=LEFT).shift(UP)
        
        self.play(
            FadeIn(title2),
            Write(title),
            FadeIn(defBern)
        )

        # Slide 4
        self.play(FadeIn(slide_counter[counter]))
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1

        self.play(
            FadeOut(title),
            FadeOut(defBern)
        )


        titledef2 = Text(r"Определение 2.", weight=BOLD).to_corner(UL).shift(1.15 * DOWN + 0.25 * RIGHT)
        defKraw = VGroup(
            Tex(r"Многочлен \((1+x)^{n-r}(1-x)^{r}\) является производящей функцией для многочленов Кравчука:", tex_environment='flushleft').scale(0.7),
            MathTex(r"(1+x)^{n-r}(1-x)^r = \sum_{s=0}^{n} K_s^{(n)} (r) \, x^s.").scale(0.7)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).shift(UP)
        
        self.play(
            Write(titledef2),
            FadeIn(defKraw)
        )

        # Slide 5
        self.play(FadeIn(slide_counter[counter]))
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1
        self.play(
            FadeOut(titledef2),
            FadeOut(defKraw),
            FadeOut(title2)
        )

        trivial = VGroup(
            Tex(r"В силу соотношения", tex_environment='flushleft').scale(0.7),
            MathTex(r"(1+x)^{n-r}(1-x)^r = (1+t)^{n - (n - r)}(1-t)^{n-r} = \sum_{s=0}^{n} K_s^{(n)} (n-r) \, x^s").scale(0.7),
            Tex(r"и замены \(x = \frac{t+1}{2}\) формула для многочленов Бернштейна преобразуется следующим образом.", tex_environment='flushleft').scale(0.7)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).shift(2*UP + 4*LEFT)
        
        self.play(FadeIn(trivial))

        self.play(FadeIn(slide_counter[counter]))
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1

        # Slide 6
        self.play(FadeOut(trivial))

        formulas = [MathTex(r"B_n(f; \, x)"), MathTex(r"B_n(f; \, x) = \sum_{r=0}^{n} \binom{n}{r} f_r x^r (1-x)^{n-r}"), MathTex(r"B_n (f; \, t) = \sum_{r = 0}^{n}  \binom{n}{r} f_r \,\left(\frac{1+t}{2}\right)^r \left(\frac{1-t}{2}\right)^{n-r}"), MathTex(r"B_n (f; \, t) = \frac{1}{2^n}\sum_{r = 0}^{n}  \binom{n}{r} f_r \,(1+t)^r (1-t)^{n-r}"),
                    MathTex(r"B_n (f; \, t) = \frac{1}{2^n} \sum_{r=0}^{n} \binom{n}{r} f_{n-r} \sum_{s = 0}^{n} K_s^{(n)} (n-r) t^s"), MathTex(r"B_n (f; \, t) = \frac{1}{2^n} \sum_{s = 0}^{n} \left( \sum_{r=0}^{n} \binom{n}{r} \; f_{n-r} K_s^{(n)} (r)\right) \cdot t^s")]

        # Slides 7-11
        for f in zip(formulas, formulas[1:]):
            self.play(
                TransformMatchingShapes(
                    f[0], f[1]
                )
            )
            self.play(FadeIn(slide_counter[counter]))
            self.next_slide()
            self.play(FadeOut(slide_counter[counter]))
            counter += 1
        
        titledef3 = Text(r"Определение 3.", weight=BOLD).to_corner(UL).shift(1.15 * DOWN + 0.25 * RIGHT)
        defMW = VGroup(
            Tex(r"Квадратная \((n+1) \times (n+1)\)-матрица \(M_n\), где", tex_environment='flushleft').scale(0.7),
            MathTex(r"(M_n)_{ij} = K_{i}^{(n)}(j), \quad 0 \leq i, \, j \leq n").scale(0.7),
            Tex(r"называется матрицей Мак-Вильямс порядка \(n\).", tex_environment='flushleft').scale(0.7),
            Tex(r"Для любого вектор-столбца \(u = (u_0, \, u_1, \, \dots, \, u_n)\) длины \((n+1)\) его преобразование Мак-Вильямс порядка \(n\) определяется как произведение", tex_environment='flushleft').scale(0.7),
            MathTex(r"\mathcal{M}_n(u) = M_n \, u.")
        ).arrange(DOWN, center=False, aligned_edge=LEFT).shift(2*LEFT+UP)
        
        self.play(
            FadeOut(formulas[-1]),
            Write(titledef3),
            FadeIn(defMW)
        )

        # Slide 12
        self.play(FadeIn(slide_counter[counter]))
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1

        self.play(
            FadeOut(titledef3),
            FadeOut(defMW)
        )
        transform_title = Title(r"Многочлены Бернштейна и преобразование Мак-Вильямс")
        self.play(FadeIn(transform_title))
       
        Defapp = Tex(r"Пусть \(^\beta f = \left(\binom{n}{r} \cdot f_{n-r} \right)^{T}_{0 \leq r \leq n}\) и пусть \(\mathfrak{T}_{n}(f)\) вектор коэффициентов многочлена Бернштейна \(B_n (f; \, t)\).\\Тогда", tex_environment = 'flushleft').scale(0.7).shift(2*UP+1.25*LEFT)
        Basis = MathTex(r"\mathfrak{T}_n(f) = \frac{1}{2^n}\mathrm{M}_n \, ^\beta f,").scale(0.7).shift(UP)
        FinalFormulae = VGroup(
            Tex(r"то есть \(\mathfrak{T}_n(f) = \frac{1}{2^n}\mathcal{M}_n (^\beta f)\), и, следовательно,", tex_environment='flushleft').scale(0.7).shift(0.35 * UP + 3 * LEFT),
        ).arrange(DOWN, center=False, aligned_edge=LEFT)

        basis_bern = MathTex(r"B_n (f; \, t) = \frac{1}{2^n}\sum_{s=0}^{n} (\mathcal{M}_n (^\beta f))_s t^{s}").scale(0.7).shift(0.75 * DOWN)
        
        conclusion = Tex(r"--- формула для многочленов Бернштейна в степенном базисе через преобразование Мак-Вильямс.", tex_environment='flushleft').scale(0.7).shift(2 * DOWN + 1.25 * LEFT)

        # Slide 13
        self.play(FadeIn(Defapp, FinalFormulae, conclusion), Write(VGroup(Basis, basis_bern)))
        self.play(FadeIn(slide_counter[counter]))
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1
        
        self.play(FadeOut(Defapp), FadeOut(FinalFormulae, transform_title, conclusion, Basis, basis_bern))
        title3 = Title("Пирамида Паскаля-Мак-Вильямс")

        pyr1 = Tex(r"Множество всех матриц Мак-Вильямс может быть представлено как трехмерная пирамида с помощью следующего рекуррентного соотношения:", tex_environment='flushleft').scale(0.7).shift(2*UP+1*LEFT)


        pyramid = MathTex(r"M_{n+1} = \left(\underline{M_n|} + \overline{M_n|} + \underline{|M_n} - \overline{|M_n} \right)\cdot \mathrm{diag}(1, \, 1/2, \, \dots, \, 1/2, \, 1),\\  n\geq 0, \;M_0 = [1].").scale(0.7).shift(0.25 * UP)


        pyr2 = Tex(r"Способ построения подобен стандартному построению треугольника Паскаля.", tex_environment='flushleft').scale(0.7).shift(2 * DOWN + 1 * LEFT)

        # Slide 14
        self.play(FadeIn(pyr1, pyr2, title3), Write(pyramid))
        self.play(FadeIn(slide_counter[counter]))
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1

        self.play(FadeOut(pyr1, pyr2, title3, pyramid))

        self.play(FadeIn(slide_counter[counter]))
        mws = [ImageMobject(mw.MWplot(i, 17)) for i in range(2, 170)]
        for i, img in enumerate(mws):
            img.height = 3+3*(1.5*i/170)
            img.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        print(mws)
        for img in mws:
            self.add(img)
            self.play(FadeIn(img, run_time = 20/160))

        # Slide 15
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
 
        title4 = Title("Приложение метода к многочленам Чебышева первого рода")

        chebintro = Tex(r"Многочлен Чебышева первого рода \(T_n(x)\) порядка \(n\) есть многочлен степени \(n\) такой, что", tex_environment='flushleft').scale(0.7).shift(2*UP+1*LEFT)


        cheb = MathTex(r"T_n (\cos \alpha) = \cos n \alpha.").scale(0.7).shift(0.75 * UP)


        chebcon = Tex(r"Наш метод применим также и к многочленам Чебышева первого рода. Формула многочленов Чебышева порядка \(n\) в степенном базисе", tex_environment='flushleft').scale(0.7).shift(0.5 * DOWN + 1 * LEFT)


        chebkraw = MathTex(r"T_n(x) = \frac{1}{2^n}\sum_{s=0}^{n} \left(\sum_{k = 0}^{n}(-1)^{k} \binom{2n}{2k}  K_{s}^{(n)}(k) \right) x^{s}.").scale(0.7).shift(1.5 * DOWN)
        self.play(FadeIn(title4, chebcon, chebintro), Write(cheb), Write(chebkraw))
        self.play(FadeIn(slide_counter[counter]))

        # Slide 16
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1

        self.play(FadeOut(chebcon, chebintro, cheb))



        chebcoll = Tex(r"Из чего выводится элементарное следствие. Пусть \(p > 2\) --- простое число, тогда", tex_environment='flushleft').scale(0.7).shift(0.25 * DOWN + 0.75 * LEFT)

        chebprime = MathTex(r"T_p(x) \equiv x \mod p.").scale(0.7).shift(DOWN)

        self.play(chebkraw.animate.shift(2.5 * UP))
        self.play(FadeIn(chebcoll), Write(chebprime))
        self.play(FadeIn(slide_counter[counter]))

        # Slide 17
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1

        self.play(FadeOut(chebcoll, chebkraw, chebprime, title4))

        title5 = Title("Заключение: клеточные автоматы")

        cell = Tex("Аналогично тому, что треугольник Паскаля можно рассматривать, как результат последовательных состояний некоторого одномерного линейного клеточного автомата, пирамиду Паскаля-Мак-Вильямс также можно интерпретировать как результат работы подобного, но уже двумерного, автомата, что в свое время (2004) было представлено научным руководителем автора настоящей работы в Wolfram Library Archive: \\url{https://library.wolfram.com/infocenter/MathSource/5223/}.", tex_environment='flushleft').scale(0.75)

        self.play(FadeIn(cell, title5))

        # Slide 18
        self.play(FadeIn(slide_counter[counter]))
        self.next_slide()
        self.play(FadeOut(slide_counter[counter]))
        counter += 1
        
        self.play(FadeOut(cell, title5))

        title_last = Title("Заключение")

        solutions = VGroup(
            Tex("Основные результаты, полученные в ходе работы."),
            Tex("1. Разработан новый подход для вычисления коэффициентов многочленов Бернштейна.", tex_environment = 'flushleft'),
            Tex("2. Представлено приложение данного подхода к многочленам Чебышева.", tex_environment = 'flushleft'),
            Tex("3. Разработаны программы для вычисления матриц Мак-Вильямс и создания демонстрационного материала по теме исследования.", tex_environment = 'flushleft'),
            Tex("Результаты работы были представлены на конференции Polynomial Computer Algebra 2023 в Санкт-Петербурге и опубликованы в тезисах \\url{https://pca-pdmi.ru/2023/files/17/Gogin-Shubin-2023.pdf}.", tex_environment = 'flushleft')
        ).arrange(DOWN, center = False, aligned_edge=LEFT).shift(3*LEFT + 3*UP).scale(0.7)

        self.play(FadeIn(slide_counter[counter], title_last, solutions))
