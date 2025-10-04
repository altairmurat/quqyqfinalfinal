from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import GptResponse, Course, Lesson, Material, Book

def seed_database():
    # Create tables if not already created
    Base.metadata.create_all(bind=engine)

    # Create a new database session
    db = SessionLocal()
    try:
        # Check if courses already exist to avoid duplicates
        if db.query(Course).count() == 0:
            # Insert Courses
            courses = [
                Course(id=1, name="NIS Program Quqyq"),
                Course(id=2, name="Olympiad Preparation"),
                Course(id=3, name="External resources for preparing")
            ]
            db.add_all(courses)

            # Insert Lessons for 1st Course
            lessons = [
                Lesson(course_id=1, title="1-сабақ", pdf_lesson="https://drive.google.com/file/d/1Ad2ziTSYjHpCfggcQeu4a11f_CYRerti/preview", video_url="https://drive.google.com/file/d/15sDJwNLDxKCEDk4XlnlXK7rWjftmNZ8c/preview", pdf_answers="https://drive.google.com/file/d/1fn-hqUdp8PS5pZvI4G-qnVshQjmRE-lg/preview", transcript='<h1>Құқық дегеніміз не және ол қоғамдағы қарым-қатынастарға қалай әсер етеді?</h1><p>Әлеуметтік нормалар – бұл адамдардың мінез-құлқын және қоғамдық өмірді реттейтін, сонымен қатар қоғамның тұрақтылығы мен тұтастығын нығайтатын ережелер.</p><p>Мораль – адамның мінез-құлқының адамгершілік нормалары. Ол адамның іс-әрекетін жақсы мен жаман, ізгілік пен зұлымдық тұрғысынан бағалайды. Бірақ бұл ережелер ресми құжаттарда бекітілмегенімен, қоғамның барлық мүшелеріне қатысты.</p><p>Құқық – бұл мемлекетпен белгіленген немесе мойындалған және оның мәжбүрлеу күшімен қамтамасыз етілетін жалпыға міндетті мінез-құлық нормаларының жүйесі.</p><p>Қарапайым тілмен айтқанда: құқық – бұл қоғам өмір сүретін және мемлекет қорғайтын ережелер.</p><h4>Құқық пен моральдың айырмашылықтары:</h4><table><tr><th>Критерий</th><th>Құқық</th><th>Мораль</th></tr><tr><td>Бастау көзі</td><td>Мемлекет белгілейді (заңдар, кодекстер, Конституция)</td><td>Қоғамда дәстүрлерден, мәдениеттен, діннен туындайды</td></tr><tr><td>Форма</td><td>Жазбаша түрде бекітіледі және мемлекеттік, заң шығарушы деңгейде қабылданады</td><td>Ресми формасы жоқ, әдет-ғұрыптарда және адамдардың санасында өмір сүреді</td></tr><tr><td>Қамтамасыз ету</td><td>Мемлекеттің күшімен қолданылады, бұзған жағдайда жаза қолданылады (айыппұл, қамау)</td><td>Қоғамдық пікірмен, қоғаммен, адамның ар-ұжданымен қолдау табады</td></tr><tr><td>Бұзғаны үшін санкция</td><td>Құқықтық жауапкершілік (айыппұл, түрме, құқық/бостандықтан айыру)</td><td>Қоғамның айыптауы, сый-құрметтен айырылу, кінә сезімі</td></tr><tr><td>Әрекет ету аясы</td><td>Қоғамдық маңызды қатынастарды реттейді (саясат, экономика, еңбек)</td><td>Күнделікті мінез-құлқын, адамдар арасындағы қатынастарды реттейді</td></tr><tr><td>Сипаты</td><td>Жалпыға міндетті, ресми түрде айқын</td><td>Жалпыға міндетті, бірақ икемді, мәдениетке және уақытқа байланысты өзгереді</td></tr><tr><td>Сақтаудың мотивациясы</td><td>Жазадан қорқу, құқықты қорғау</td><td>Ар-ұждан, сый-құрметке ұмтылу, «жақсы адам болу» тілегі</td></tr><tr><td>Мысал</td><td>Салық төлемеу, көлік жүргізгенде жылдамдықты асыру → мемлекеттен айыппұл</td><td>Автобуста үлкенге орын бермеу, амандаспау → адамдардың айыптауы</td></tr></table><div class="tree-diagram"><div class="tree-top">Әлеуметтік нормалар</div><div class="tree-line"></div><div class="horizontal-line"></div><div class="tree-branches"><div class="tree-branch">Құқық</div><div class="tree-branch">Мораль</div></div></div><h4>Құқық пен моральдың ұқсастықтары:</h4><ul><li>Екеуі де адамдардың мінез-құлқын реттейді.</li><li>Екеуі де қоғамның барлық мүшелері үшін міндетті.</li><li>Екеуі де ізгілік, әділеттілік, адалдық құндылықтарына негізделген.</li><li>Екеуі де тәртіп пен тұрақтылықты нығайтуға бағытталған.</li><li>Екеуі де жеке тұлға мен қоғам мүдделерін қорғайды.</li><li>Екеуі де қоғаммен бірге пайда болып, дамиды.</li><li>Екеуі өзара байланысты: мораль көбіне құқықтың негізі болады.</li></ul><p>Мораль құқықтан бұрын пайда болды.</p><p>Мораль алғашқы адам қауымдарында әдет-ғұрыптар, тыйымдар мен мінез-құлық нормалары (не жақсы, не жаман) ретінде табиғи түрде пайда болды. Бұл топтың өмір сүруі мен келісімді өмірі үшін қажет болды, мемлекеттің пайда болуынан әлдеқайда бұрын.</p><p>Құқық кейінірек, мемлекетпен бірге пайда болды. Қоғам үлкен әрі күрделі болған сайын, мінез-құлық нормаларын тек дәстүр түрінде емес, билік пен жазамен қамтамасыз етілетін ресми заң түрінде бекіту қажеттілігі туындады.</p><h4>Мысалдар:</h4><ul><li>Алғашқы адамдарда мораль нормалары болды — руластарыңды өлтіруге болмайды, олжаңды бөлісу керек.</li><li>Бірақ жазбаша заңдар («Жеті Жарғы» Тәуке ханының заңдары, Қасым ханның «Қасқа жолы», Есім ханның «Ескі жолы», адаттар, қазіргі ҚР заңдары) кейінірек пайда болды.</li></ul><div class="diagram"><div class="diagram-box">Мораль</div><span class="diagram-arrow">→</span><div class="diagram-box">Құқық</div></div><p>Құқық пен моральдың байланысы:</p><h4>1. Мораль: «Балаларды ренжітпеу, кішілерге қамқор болу».</h4><p>Құқық: ҚР Конституциясы (27-бап) – балаларға қамқорлық жасау, тәрбиелеу – ата-ананың табиғи құқығы мен міндеті. Сондай-ақ «Қазақстан Республикасындағы баланың құқықтары туралы» Заң бар.</p><h4>2. Мораль: «Ата-ананы, үлкендерді құрметтеу».</h4><p>Құқық: ҚР Конституциясы (27-бап) – кәмелетке толған балалар еңбекке жарамсыз ата-анасына қамқорлық жасауға міндетті.</p><h4>3. Мораль: «Адам өлтірмеу, зиян келтірмеу».</h4><p>Құқық: ҚР Қылмыстық кодексі – кісі өлтіру, дене жарақатын салу, азаптау – қатаң жазаланады.</p><h4>4. Мораль: «Ұрлық жасамау, бөтеннің мүлкін құрметтеу».</h4><p>Құқық: ҚР Конституциясы (26-бап) – жеке меншікке қол сұғылмаушылық бекітілген; Қылмыстық кодексте ұрлық, тонау, қарақшылық – қылмыстық істер.</p><h4>5. Мораль: «Адал болу, өтірік айтпау».</h4><p>Құқық: ҚР Қылмыстық кодексінде жалған куәлік беру, алаяқтық, құжаттарды қолдан жасау үшін жауапкершілік көзделген.</p><h4>6. Мораль: «Әлсіздер мен мұқтаждарға қамқор болу».</h4><p>Құқық: ҚР Конституциясы (28-бап) – азаматтардың жасына, сырқатына, мүгедектігіне, асыраушысынан айырылуына байланысты әлеуметтік қамсыздандыру құқығы бекітілген.</p><h4>7. Мораль: «Отанды сүю, қорғау».</h4><p>Құқық: ҚР Конституциясы (36-бап) – Қазақстан Республикасын қорғау – әрбір азаматтың міндеті.</p><br><br><h1>Ендіше тапсырмалар орындаңыз!</h1><br><div class="task"><h1>1 Тапсырма:</h1><div class="kazakh"><p>Қоғамда өмір сүретін адамдардың өздерін ұстау ережелерінің жиынтығын <input type="text" class="fill-blank" id="task1_1"> деп атаймыз.</p><p>Адам тәртібінің конвенционалды нормалары деп <input type="text" class="fill-blank" id="task1_2"> айтамыз.</p><p>Құқықтың пайда болуы <input type="text" class="fill-blank" id="task1_3"> пайда болуымен байланысты.</p><p>Мемлекет тарапынан заңдастырылған және қорғалатын, жалпыға бірдей міндетті нормалар жүйесін <input type="text" class="fill-blank" id="task1_4"> деп атаймыз.</p><p><input type="text" class="fill-blank" id="task1_5"> – мемлекеттің негізгі заңы.</p><p>Нормативтік құқықтық актілерге <input type="text" class="fill-blank" id="task1_6"> жатады.</p><p>Қажетті сөздер: Мемлекет. Құқық. Заң. Нормативтік актілер. Әлеуметтік нормалар. Мораль</p></div><button onclick="checkTask1()">Тексеру</button><div id="result1"></div></div><div class="task"><h1>2 Тапсырма: Венн диаграмма арқылы мораль мен құқықтың айырмашылығы мен ұқсастықтарын талдаңыз.</h1><div class="venn-container"><div class="circle left-circle">Мораль</div><div class="circle right-circle">Құқық</div></div></div><div class="task"><h1>3 Тапсырма:</h1><div class="kazakh"><p>Елімізде құқық бұзушылықтардың орын алу себептері азаматтардың заңдарды білмеуінен бе, әлде құқықтық мәдениеттің төмен болуынан ба? ПТМС бойынша.</p><p> Позиция: <input type="text" class="fill-blank" id="task3_1"></p><p> Түсіндіру (себебі...): <input type="text" class="fill-blank" id="task3_2"></p><p> Мысал (мен мұны мынадай мысал арқылы дәлелдей аламын...): <input type="text" class="fill-blank" id="task3_3"></p><p> Салдар (айтылған мәселе бойынша мынандай қорытынды жасаймын...): <input type="text" class="fill-blank" id="task3_4"></p></div></div>'),
                Lesson(course_id=1, title="2-сабақ", pdf_lesson="https://drive.google.com/file/d/1VcwElMvlm9iVAkJ17encLzuxmn42DyDX/preview", pdf_answers="https://drive.google.com/file/d/1gFmpc5dWD6lHgcv3QGu-6AQ3MW5lCnUl/preview", transcript="Төменде екінші сабақ бойынша конспектпен таныссаңыздар болады."),
                Lesson(course_id=1, title="3-сабақ", pdf_lesson="https://drive.google.com/file/d/10hd5fs0bsgI1dEMzjsAB8e7WZFlUJVgB/preview", pdf_answers="https://drive.google.com/file/d/1a8C21EnrQSQ9dWydJxAKYj8cf2YXrVZO/preview", transcript="Төменде үшінші сабақ бойынша конспектпен таныссаңыздар болады."),
                Lesson(course_id=1, title="4-сабақ", pdf_lesson="https://drive.google.com/file/d/1lI8jWHggD4-NiBOyuLwOiS-L0XNr01ET/preview", pdf_answers="https://drive.google.com/file/d/1en32Uz4EH1IYziLBwyQfQVIoRCjfJzGi/preview", transcript="Төменде төртінші сабақ бойынша конспектпен таныссаңыздар болады."),
                Lesson(course_id=1, title="5-сабақ", pdf_answers="https://drive.google.com/file/d/1iaqiHREEyhq_9IJ4GhAqbFnefe2ACu2F/preview", transcript="Төменде бесінші сабақ бойынша конспектпен таныссаңыздар болады."),
                Lesson(course_id=1, title="6-сабақ", pdf_lesson="https://drive.google.com/file/d/1rTj_ZT-jtZOSVL0KvU2IxPhUHvB5OzPG/preview", transcript="Transcript 6...")
            ]
            db.add_all(lessons)

            # Insert Materials for 2nd Course
            materials = [
                Material(course_id=2, title="Material 1", pdf_url="http://example.com/material1.pdf"),
                Material(course_id=2, title="Material 2", pdf_url="http://example.com/material2.pdf")
            ]
            db.add_all(materials)

            # Insert Books for 3rd Course
            books = [
                Book(course_id=3, title="Book 1", pdf_url="http://example.com/book1.pdf"),
                Book(course_id=3, title="Book 2", pdf_url="http://example.com/book2.pdf")
            ]
            db.add_all(books)

            # Commit the changes
            db.commit()
            print("Database seeded successfully!")
        else:
            print("Database already contains courses, skipping seeding.")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()