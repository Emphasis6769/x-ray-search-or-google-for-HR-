# Глава 10 задача 1

# GUI с другим содержанием блоков
# Сделать такого же сказочника только расположить обьекты по другому
# Мне нужен GUI (связанный с подбором персонала и составления X-ray запроса)

# В начале бросим инструкцию текстом
# Параметры
 # Сайт для поиска (линк, фб, вк, инст) - "флажки" (1 выбор, скорее переключатели)
  # Выбор страны (гражданства) - флажки (много выборов)
   # Выбор города - текстовое поле
    # Специализация человека - тектовое поле (уже нет кажется)
     # Ключевые навыки - текстовое поле с написанием через пробел
      # (выделение их через знак & - отделим добавим)
      # Выбор сферы предыдущих работ флажки много выбора - (банк, IT и т.д.)
       # Образование - текстовое поле
        # Проекты (название их - пример "Яндекс.Еда" ) - текстовое поле
         # Сертификаты - текстовое поле
# Кнопка вывод результата
# Текстовое поле в которое выведется конечный X-ray запрос
 # Если получиться то кнопка что скопирует текст в буфер обмена

# Импортируем Ткинтер
 # напишем класс Аппликейшн
  # отцовкий констурктор __init__
   # функция создание виджетов по очереди
# Прописать модуль транслитерации дополнительно, переводчик врятли

# Создание окна (название и размер), запуск класса, запустить цикл


from tkinter import *

class Applicatione (Frame):
    # Создание Рамки
    def __init__(self,master):
        super(Applicatione,self).__init__(master)
        self.grid()
        self.create_vedgets()
        self.kart = () # для доп навыков
        self.comp = () # для предыдущих проектов
        self.ist_vars = [] #для сертификатов


        # Создадим все виджеты
    def create_vedgets(self):
        # Инструкция
        Label(self,
             text="Инструкция: Программа помогает составить X-ray запрос для поиска персонала."
                  "Введи все параметры и скопируйте текст в Google поисковик. Не вводите более 30 параметров."
             ).grid(row=0,column=0,columnspan=12, sticky=W)

        # 1-1 Сайты для поиска (флаги)
        Label(self,
              text='Выберите сайт на котором будем искать:'
              ).grid(row=1,column=0,sticky=W)

        # 1-2 Сайты для поиска
        self.site = StringVar()
        self.site.set("")
        sites = (('Linkedin',"linkedin.com"),('Github',"github.com"),('Stack Overflow',"stackoverflow.com"),
                 ('Habr',"habr.com"),('Instagram',"instagram.com"),('Facebook',"facebook.com"),('Vk',"vk.com"),
                 ('Сетка',"setka.hh.ru"),('Telegram',"telegram.org"))
        column = 0
        for i in sites:
            Radiobutton(self,text=i[0],
                        variable=self.site,
                        value=i[1],
                        ).grid(row=2,column=column,sticky=W)
            column +=1

        # 1-3 Выбор Страны (гражданства) флаги
        self.vars = [] #хранилище всех флагов
        self.selected = [] #будущие выбранные страны
        self.countries = (("Россия", "Russia"), ("Беларусь", "Belarus"), ("Украина", "Ukraine"), ("Грузия", "Georgia"),
                          ("Армения", "Armenia"), ("Азербайджан", "Azerbaijan"), ("Казахстан", "Kazakhstan"),
                          ("Таджикистан", "Tajikistan"), ("Узбекистан", "Uzbekistan"), ("Туркменистан", "Turkmenistan"),
                          ("Киргизия", "Kirgyzstan"))

        Label(self,text='Страна проживания').grid(row=3,column=0,sticky=W)

        def create_widgets_str():
            # Все флаги
            column = 0
            for i, country in enumerate(self.countries):  # enumerate дает i значение индекса запрашиваемой переменной
                # и саму переменную
                var = BooleanVar(value=False)  # хранилище флага (одного)
                self.vars.append(var)  # собирает все переменные в self.vars для массового использования

                cb = Checkbutton(self, text=country[0],
                                 variable=var,
                                 command=lambda i=i: update_selected_countries(i)
                                 # комманд с функцией для назначения x-ray слова
                                 ).grid(row=4, column=column, sticky=W)
                column += 1

            def update_selected_countries(idx=None):
                self.selected = [self.countries[i] for i, v in enumerate(self.vars) if v.get()]

        create_widgets_str()


        # Выбор города проживания
        Label(self,text='Введите город проживания специалиста').grid(row=5,column=0,sticky=W)

        self.gorod = Entry(self)
        self.gorod.grid(row=5,column=1,sticky=W)

        # Выбор образования (уровень + направление)
         # это 2 набора флагов Checkbutton

        # Среднее
        self.obr_sre=BooleanVar()
        Checkbutton(self, text='Среднее образование',
                     variable=self.obr_sre
                     ).grid(row=6,column=0,sticky=W)
        # бакалавриат
        self.obr_bach=BooleanVar()
        Checkbutton(self,text='Бакалавриат',
                    variable=self.obr_bach
                    ).grid(row=6,column=1,sticky=W)
        # магистратура
        self.obr_mag=BooleanVar()
        Checkbutton(self,text='Магистратура',
                    variable=self.obr_mag
                    ).grid(row=6,column=2,sticky=W)
        # PHD
        self.obr_phd=BooleanVar()
        Checkbutton(self,text='Доктор наук',
                    variable=self.obr_phd
                    ).grid(row=6,column=3,sticky=W)


        # Направление # потом можно переписать через словарь и перебор
        self.napr_sys_eng=BooleanVar()
        sys_eng_ru = 'Системная инженерия'
        sys_eng_eng = 'System Engineering'
        Checkbutton(self,text=sys_eng_ru,
                    variable=self.napr_sys_eng,
                    ).grid(row=7,column=0,sticky=W)

        self.napr_cy_sec = BooleanVar()
        cy_sec_ru = 'Кибербезопасность'
        cy_sec_eng = 'Cybersecurity'
        Checkbutton(self, text=cy_sec_ru,
                    variable=self.napr_cy_sec,
                    ).grid(row=7, column=1, sticky=W)

        self.napr_dat_sci = BooleanVar()
        dat_sci_ru = 'Data Science'
        dat_sci_eng = 'Data Science'
        Checkbutton(self, text=dat_sci_ru,
                    variable=self.napr_dat_sci,
                    ).grid(row=7, column=2, sticky=W)

        self.napr_bus_anal = BooleanVar()
        bus_anal_ru = 'Бизнес-аналитика'
        bus_anal_eng = 'Business Analytics'
        Checkbutton(self, text=bus_anal_ru,
                    variable=self.napr_bus_anal,
                    ).grid(row=7, column=3, sticky=W)

        self.napr_data_anal = BooleanVar()
        data_anal_ru = 'Аналитика данных'
        data_anal_eng = 'Data Analytics'
        Checkbutton(self, text=data_anal_ru,
                    variable=self.napr_data_anal,
                    ).grid(row=7, column=4, sticky=W)

        self.napr_b_data_anal = BooleanVar()
        b_data_anal_ru = 'Аналитика больших данных'
        b_data_anal_eng = 'Big Data Analytics'
        Checkbutton(self, text=b_data_anal_ru,
                    variable=self.napr_b_data_anal,
                    ).grid(row=7, column=5, sticky=W)

        self.napr_dat_eng = BooleanVar()
        dat_eng_ru = 'Инженерия данных'
        dat_eng_eng = 'Data Engineering'
        Checkbutton(self, text=dat_eng_ru,
                    variable=self.napr_dat_eng,
                    ).grid(row=7, column=6, sticky=W)

        self.napr_mach_learn = BooleanVar()
        mach_learn_ru = 'Машинное обучение'
        mach_learn_eng = 'Machine Learning'
        Checkbutton(self, text=mach_learn_ru,
                    variable=self.napr_mach_learn,
                    ).grid(row=7, column=7, sticky=W)

        self.napr_deep_learn = BooleanVar()
        deep_learn_ru = 'Глубокое обучение'
        deep_learn_eng = 'Deep Learning'
        Checkbutton(self, text=deep_learn_ru,
                    variable=self.napr_deep_learn,
                    ).grid(row=7, column=8, sticky=W)

        self.napr_nat_lang_proc = BooleanVar()
        nat_lang_proc_ru = 'Обработка естественного языка'
        nat_lang_proc_eng = 'Natural Language Processing'
        Checkbutton(self, text=nat_lang_proc_ru,
                    variable=self.napr_nat_lang_proc,
                    ).grid(row=7, column=9, sticky=W)

        # Специализация человека наверное сделаем через переключатель (радиобуттон)
        Label(self,text='Специализация'
              ).grid(row=8,column=0,sticky=W)

        specializations=('Software Developer','Web Developer','Mobile Developer','Game Developer','System Administrator','Network Administrator','Cybersecurity Specialist','Data Analyst','Data Engineer','Machine Learning Engineer','DevOps Engineer','QA','Frontend Developer','Backend Developer')

        self.prof=StringVar()
        self.prof.set("")

        column=1
        for i in specializations:
            Radiobutton(self,text=i,
                        variable=self.prof,
                        value=i,
                        command=self.update_text, #тут апдейт переменной self.prof скорее всего должен быть
                        ).grid(row=8,column=column,sticky=W)
            column+=1

        # Уровень опыта
        Label(self,text='Уровень квалификации').grid(row=9,column=0,sticky=W)

        opit_spec=('Junior','Middle','Senior','Lead','Expert/Consultant)')

        self.opit=StringVar()
        self.opit.set("")

        column=1
        for i in opit_spec:
            Radiobutton(self,text=i,
                        variable=self.opit,
                        value=i
                        ).grid(row=9,column=column,sticky=W)
            column+=1

        # Ключевые навыки Hard (языки программирвоания)
         # Через флаги BooleanVar() + текстовое поле для других
          # в будущем хотелось бы сделать через открывающийся список
        hard_skills=(('Frontend-разработчик','HTML','CSS','JavaScript','React','Angular','Vue.js','Responsive design и адаптивная верстка','Webpack','Gulp','Grunt','UX/UI'),
                     ('Backend-разработчик','Python','Java,','C#','Ruby','PHP','Node.js','MySQL',"PostgreSQL",'MongoDB','Redis','RESTful','GraphQL','Django','Flask','Spring','Express'),
                     ('Full Stack-разработчик'," "),('Системные администратор','Windows','Linux','TCP/IP','DNS',' DHCP','настройка и администрирование серверов',
                    'мониторинг и управление производительностью','VMware','Docker','Kubernetes'),('Аналитик данных','R','SQL','Pandas','NumPy','Matplotlib','Статистика','Machine Learning','Tableau','Power BI','D3.js'),
                     ('Специалисты по кибербезопасности','Аудит','Принципы безопасности','Metasploit','Burp Suite','ISO 27001','NIST'),
                     ('QA','функцональное','регрессивное','нагрузочное','Selenium','JUnit','TestNG','Документация','JIRA','Bugzilla'),
                     ('DevOps-инженер','Jenkins','GitLab','Circle','Docker','Kubernetes','Ansible','Puppet','Chef','AWS','Azure','Google Cloud','Prometheus','Grafana','ELK Stack'),
                     ('UX/UI дизайнер','Figma','Adobe XD','Sketch','Прототипирование','wireframing','UX','UI','исследования','тестирование','HTML','CSS'))

        self.all_hard_skills= []
        row = 10
        for i in hard_skills:
            column=0
            Label(self,text=i[0]
                  ).grid(row=row,column=column,sticky=W)
            for x in i[1:]:
                self.skil=BooleanVar()
                column += 1
                Checkbutton(self,text=x,
                            variable=self.skil,
                            command=self.update_text_skill
                            ).grid(row=row,column=column,sticky=W)
                self.all_hard_skills.append((self.skil,x))
            row +=1



        # Дополнительные навыки
        Label(self,text='Дополнительные навыки'
              ).grid(row=19,column=0,sticky=W)

        # Текстовое поле, его значение через кнопку кидать в 1 переменную список
         # текстовое поле где отображались бы все 7 переменных
          # придумать механизм стирания всех 7 переменных и текста
        self.peremennaya = Entry(self)
        self.peremennaya.grid(row=19,column=1,sticky=W)

        perem = '' # хранилище переменных
        def dopolneniye():
            self.perem=self.peremennaya.get()
            x = (str(self.perem))
            self.kart
            self.kart += (x,)
            self.peremennaya.delete(0, END)
            self.pole.insert('1.0', str(self.perem))
            print('Поисковое слово добавлено!')
        def udality():
            self.perem = ''
            self.kart = ()
            print(self.kart)
            self.pole.delete('1.0', 'end')
            print('Самописные ключевые слова удалены')

        Button(self,text='Внести данные',
               command=dopolneniye
               ).grid(row=19,column=2,sticky=W)
        Button(self,text= 'Удалить',
               command=udality
               ).grid(row=19,column=3,sticky=W)

        self.pole= Text(self,width=30,height=2,wrap=WORD)
        self.pole.grid(row=19,column=4,sticky=W)
        if perem != 0:
            perem =str(perem)
            self.pole.delete(0.0,END)
            self.pole.insert(1.0,perem)



        # Сферы предыдущей работы, переключатели

        Label(self,text="Сферы предыдущей работы"
              ).grid(row=20,column=0,sticky=W)

        self.sfera=StringVar()
        self.sfera.set('')
        sfery = (
            ("Финансовый сектор", "Financial Sector"),
            ("Ритейл", "Retail"),
            ("Здравоохранение", "Healthcare"),
            ("Образование", "Education"),
            ("Телекоммуникации", "Telecommunications"),
            ("Государственный сектор", "Public Sector"),
            ("Энергетика", "Energy"),
            ("Транспорт и логистика", "Transport and Logistics"),
            ("Развлечения и медиа", "Entertainment and Media"),
            ("Производственный сектор", "Manufacturing Sector"),
            ("Недвижимость", "Real Estate"),
            ("Маркетинг и реклама", "Marketing and Advertising"),
        )

        column = 1
        for i in sfery:
            Radiobutton(self,text=i[0],
                        variable=self.sfera,
                        value=i[1]
                        ).grid(row=20,column=column,sticky=W)
            column +=1
            # command = self.update_text вырезал


        # Проекты на которых работал (текстовое поле + транслитерация когда нибудь)
        Label(self,text='Предыдущий проект'
              ).grid(row=21,column=0,sticky=W)

        self.lst_cmp = Entry(self)
        self.lst_cmp.grid(row=21,column=1,sticky=W)

        perem_pr = ''  # хранилище переменных

        def dopol():
            self.perem = self.lst_cmp.get()
            x = (str(self.perem))
            self.comp
            self.comp += (x,)
            self.lst_cmp.delete(0, END)
            # self.pole_pr.delete('1.0', 'end')
            self.pole_pr.insert('1.0', str(self.perem))
            print('Поисковое слово добавлено!')

        def udal():
            self.perem = ''
            self.comp = ()
            print(self.comp)
            self.pole_pr.delete('1.0', 'end')
            print('Самописные ключевые слова удалены')

        Button(self, text='Внести данные',
               command=dopol
               ).grid(row=21, column=2, sticky=W)
        Button(self, text='Удалить',
               command=udal
               ).grid(row=21, column=3, sticky=W)

        self.pole_pr = Text(self, width=30, height=2, wrap=WORD)
        self.pole_pr.grid(row=21, column=4, sticky=W)
        if perem_pr != 0:
            perem_pr = str(perem_pr)
            self.pole_pr.delete(0.0, END)
            self.pole_pr.insert(1.0, perem_pr)

        # Сертификаты
        # Разбивка 1) Организации 2) Специализации 3) Уровень
        # По хорошему от специализации но сделаем от организации
         # наверное попробуем при условии выбора организации отрисовывать
          # все варианты сертификатов в листбоксе (выпадающий список) чтобы можно было выбрать
        # чтобы это сделать используем переменные для хранения спец
         # сделать переключатели с компаниями, после переключения
          # команда отрисовать именно те спеиализации (на переключателях для выбора)
           # внести финальное решение в текст булеан запроса

        self.cisco_cert = (
            ("Certified Network Professional (CCNP) Collaboration", "CCNP", "Сетевое профессиональное сотрудничество (CCNP)"),
            ("Certified Internetwork Expert (CCIE) Collaboration", "CCIE", "Сертифицированный эксперт по межсетевым технологиям (CCIE) сотрудничество"),
            ("Cisco Certified Support Technician (CCST) Cybersecurity", "CCST", "Сертифицированный технический специалист Cisco (CCST) кибербезопасность"),
            ("Cisco Certified Cybersecurity Associate", "CCCA", "Ассоциированный специалист по кибербезопасности Cisco"),
            ("Cisco Certified Cybersecurity Professional", "CCCP", "Профессионал по кибербезопасности Cisco"),
            ("Cisco Certified Network Professional (CCNP) Data Center", "CCNP DC","Сетевое профессиональное сотрудничество Cisco (CCNP) Центр обработки данных"),
            ("Cisco Certified Internetwork Expert (CCIE) Data Center", "CCIE DC","Сертифицированный эксперт по межсетевым технологиям Cisco (CCIE) Центр обработки данных"),
            ("Cisco Certified Design Expert (CCDE)", "CCDE", "Сертифицированный эксперт по проектированию Cisco (CCDE)"),
            ("Cisco Certified DevNet Associate", "DevNet Associate", "Ассоциированный специалист DevNet Cisco"),
            ("Cisco Certified DevNet Professional", "DevNet Professional", "Профессионал DevNet Cisco"),
            ("Cisco Certified DevNet Expert", "DevNet Expert", "Эксперт DevNet Cisco"),
            ("Cisco Certified Support Technician (CCST) Networking", "CCST Networking","Сертифицированный технический специалист Cisco (CCST) сетевые технологии"),
            ("Cisco Certified Network Associate (CCNA)", "CCNA", "Ассоциированный сетевой специалист Cisco (CCNA)"),
            ("Cisco Certified Network Professional (CCNP) Enterprise", "CCNP Enterprise","Сетевое профессиональное сотрудничество Cisco (CCNP) Предприятие"),
            ("Cisco Certified Internetwork Expert (CCIE) Enterprise Infrastructure", "CCIE EI","Сертифицированный эксперт по межсетевым технологиям Cisco (CCIE) Инфраструктура предприятия"),
            ("Cisco Certified Internetwork Expert (CCIE) Enterprise Wireless", "CCIE EW","Сертифицированный эксперт по межсетевым технологиям Cisco (CCIE) Беспроводная сеть предприятия"),
            ("Cisco Certified Network Professional (CCNP) Security", "CCNP Security","Сетевое профессиональное сотрудничество Cisco (CCNP) Безопасность"),
            ("Cisco Certified Internetwork Expert (CCIE) Security", "CCIE Security","Сертифицированный эксперт по межсетевым технологиям Cisco (CCIE) Безопасность"),
            ("Cisco Certified Network Professional (CCNP) Service Provider", "CCNP SP","Сетевое профессиональное сотрудничество Cisco (CCNP) Поставщик услуг"),
            ("Cisco Certified Internetwork Expert (CCIE) Service Provider", "CCIE SP","Сертифицированный эксперт по межсетевым технологиям Cisco (CCIE) Поставщик услуг"),
            ("AppDynamics", "AppD", "AppDynamics"),
            ("Cisco Certified Field Technician (CCT)", "CCT", "Сертифицированный полевой техник Cisco (CCT)"),
            ("Cisco Customer Experience", "CX", "Опыт клиента Cisco"),
            ("Cisco Meraki Solutions", "Meraki", "Решения Cisco Meraki")
        )

        self.comptia_cert = (
            ("ITF+", "ITF+", "Основы ИТ (ITF+)"),
            ("Tech+", "Tech+", "Технические навыки (Tech+)"),
            ("A+", "A+", "Сертифицированный специалист по аппаратному и программному обеспечению (A+)"),
            ("Network+", "Network+", "Сетевые технологии (Network+)"),
            ("Security+", "Security+", "Кибербезопасность (Security+)"),
            ("Cloud+", "Cloud+", "Облачные технологии (Cloud+)"),
            ("CloudNetX", "CloudNetX", "CloudNetX"),
            ("Linux+", "Linux+", "Сертифицированный специалист по Linux (Linux+)"),
            ("Server+", "Server+", "Сертифицированный специалист по серверам (Server+)"),
            ("CySA+", "CySA+", "Анализ безопасности (CySA+)"),
            ("CASP+", "CASP+", "Сертифицированный опытный специалист по безопасности (CASP+)"),
            ("PenTest+", "PenTest+", "Тестирование на проникновение (PenTest+)"),
            ("Data+", "Data+", "Анализ данных (Data+)"),
            ("DataSys+", "DataSys+", "Системы данных (DataSys+)"),
            ("DataX", "DataX", "DataX"),
            ("Project+", "Project+", "Управление проектами (Project+)"),
            ("Cloud Essentials+", "Cloud Essentials+", "Основы облачных технологий (Cloud Essentials+)"),
            ("SecurityX", "SecurityX", "SecurityX")
        )

        self.microsoft_cert = (
            ("Administrator Expert", "Admin Expert", "Эксперт по администрированию"),
            ("Collaboration Communications Systems Engineer Associate", "Collab Engineer Associate",
             "Ассоциированный инженер по системам связи и сотрудничества"),
            ("Endpoint Administrator Associate", "Endpoint Admin Associate",
             "Ассоциированный администратор конечных точек"),
            ("Fundamentals", "Fundamentals", "Основы"),
            ("Teams Administrator Associate", "Teams Admin Associate", "Ассоциированный администратор Teams"),
            ("Educator", "Educator", "Сертифицированный педагог"),
            ("Azure AI Engineer Associate", "Azure AI Engineer Associate", "Ассоциированный инженер по ИИ Azure"),
            ("Azure AI Fundamentals", "Azure AI Fundamentals", "Основы ИИ Azure"),
            ("Azure Administrator Associate", "Azure Admin Associate", "Ассоциированный администратор Azure"),
            ("Azure Cosmos DB Developer Specialty", "Azure Cosmos DB Developer",
             "Специалист по разработке Azure Cosmos DB"),
            ("Azure Data Fundamentals", "Azure Data Fundamentals", "Основы данных Azure"),
            ("Azure Data Scientist Associate", "Azure Data Scientist Associate",
             "Ассоциированный специалист по данным Azure"),
            ("Azure Database Administrator Associate", "Azure DB Admin Associate",
             "Ассоциированный администратор баз данных Azure"),
            ("Azure Developer Associate", "Azure Developer Associate", "Ассоциированный разработчик Azure"),
            ("Azure Fundamentals", "Azure Fundamentals", "Основы Azure"),
            ("Azure Network Engineer Associate", "Azure Network Engineer Associate",
             "Ассоциированный инженер сетей Azure"),
            ("Azure Security Engineer Associate", "Azure Security Engineer Associate",
             "Ассоциированный инженер по безопасности Azure"),
            ("Azure Solutions Architect Expert", "Azure Solutions Architect Expert",
             "Эксперт по архитектуре решений Azure"),
            ("Azure Virtual Desktop Specialty", "Azure Virtual Desktop",
             "Специалист по виртуальному рабочему столу Azure"),
            ("Azure for SAP Workloads Specialty", "Azure for SAP", "Специалист по Azure для нагрузок SAP"),
            ("Cybersecurity Architect Expert", "Cybersecurity Architect Expert",
             "Эксперт по архитектуре кибербезопасности"),
            ("DevOps Engineer Expert", "DevOps Engineer Expert", "Эксперт по DevOps"),
            ("Dynamics Business Central Developer Associate", "Dynamics BC Developer Associate",
             "Ассоциированный разработчик Dynamics 365 Business Central"),
            ("Dynamics Business Central Functional Consultant Associate", "Dynamics BC Functional Consultant Associate",
             "Ассоциированный функциональный консультант Dynamics 365 Business Central"),
            ("Dynamics Customer Experience Analyst Associate", "Dynamics CX Analyst Associate",
             "Ассоциированный аналитик по клиентскому опыту Dynamics 365"),
            ("Dynamics Customer Service Functional Consultant Associate", "Dynamics CS Functional Consultant Associate",
             "Ассоциированный функциональный консультант по обслуживанию клиентов Dynamics 365"),
            ("Dynamics Field Service Functional Consultant Associate", "Dynamics FS Functional Consultant Associate",
             "Ассоциированный функциональный консультант по полевым услугам Dynamics 365"),
            ("Dynamics Finance Functional Consultant Associate", "Dynamics Finance Functional Consultant Associate",
             "Ассоциированный функциональный консультант по финансам Dynamics 365"),
            ("Dynamics Fundamentals (CRM)", "Dynamics CRM Fundamentals", "Основы Dynamics 365 (CRM)"),
            ("Dynamics Fundamentals (ERP)", "Dynamics ERP Fundamentals", "Основы Dynamics 365 (ERP)"),
            ("Dynamics Supply Chain Management Functional Consultant Associate",
             "Dynamics SCM Functional Consultant Associate",
             "Ассоциированный функциональный консультант по управлению цепочками поставок Dynamics 365"),
            ("Dynamics Supply Chain Management Functional Consultant Expert",
             "Dynamics SCM Functional Consultant Expert",
             "Эксперт по функциональному консультированию в управлении цепочками поставок Dynamics 365"),
            (
            "Dynamics: Finance and Operations Apps Developer Associate", "Dynamics Finance and Ops Developer Associate",
            "Ассоциированный разработчик приложений Finance and Operations Dynamics 365"),
            ("Dynamics: Finance and Operations Apps Solution Architect Expert",
             "Dynamics Finance and Ops Architect Expert",
             "Эксперт по архитектуре решений Finance and Operations Dynamics 365"),
            ("Fabric Analytics Engineer Associate", "Fabric Analytics Engineer Associate",
             "Ассоциированный инженер по аналитике Fabric"),
            ("Fabric Data Engineer Associate", "Fabric Data Engineer Associate",
             "Ассоциированный инженер по данным Fabric"),
            ("Identity and Access Administrator Associate", "Identity and Access Admin Associate",
             "Ассоциированный администратор идентификации и доступа"),
            ("Information Protection and Compliance Administrator Associate", "Info Protection Admin Associate",
             "Ассоциированный администратор защиты информации и соблюдения норм"),
            ("Information Security Administrator Associate (beta)", "Info Security Admin Associate",
             "Ассоциированный администратор информационной безопасности (бета)"),
            ("Power Automate RPA Developer Associate", "Power Automate Developer Associate",
             "Ассоциированный разработчик RPA Power Automate"),
            ("Power BI Data Analyst Associate", "Power BI Analyst Associate",
             "Ассоциированный аналитик данных Power BI"),
            ("Power Platform Developer Associate", "Power Platform Developer Associate",
             "Ассоциированный разработчик Power Platform"),
            ("Power Platform Functional Consultant Associate", "Power Platform Functional Consultant Associate",
             "Ассоциированный функциональный консультант Power Platform"),
            ("Power Platform Fundamentals", "Power Platform Fundamentals", "Основы Power Platform"),
            ("Power Platform Solution Architect Expert", "Power Platform Architect Expert",
             "Эксперт по архитектуре решений Power Platform"),
            ("Security Operations Analyst Associate", "Security Operations Analyst Associate",
             "Ассоциированный аналитик операций безопасности"),
            ("Security, Compliance, and Identity Fundamentals", "Security Compliance Identity Fundamentals",
             "Основы безопасности, соблюдения норм и идентификации"),
            ("Windows Server Hybrid Administrator Associate", "Windows Server Hybrid Admin Associate",
             "Ассоциированный администратор гибридного Windows Server")
        )

        # Иные курсы добавим позже по возможности

        # Переключатели
        Label(self,text='Cертификаты.'
              ).grid(row=22,column=0,sticky=W)

        Label(self, text='1) Выберите компанию предоставлюющую курсы, для подгрузики списка сертификатов\n'
                         '2) Далее выберите необходимые сертификаты и нажмите кнопку "Выбрать"'
              ).grid(row=22, column=1,columnspan=4, sticky=W)

        # 1 часть: КНОПКИ ДЛЯ ВЫБОРА КОМПАНИЙ ВЫДАЮЩЕЙ СЕРТИФИКАТЫ

        def naznacheniye_cert():
            """подгрузка списка курсов для листбокса, КНОПКИ"""
            sel = crtfcts.get()
            del_curs()
            if sel == 'Cisco':
                del_curs()
                self.cert = self.cisco_cert
            elif sel == 'Comptia':
                del_curs()
                self.cert = self.comptia_cert
            elif sel == 'Microsoft':
                del_curs()
                self.cert = self.microsoft_cert
            else:
                self.cert = []
                print('Биг факинг ошибка с курсами')

            for i in self.cert:
                self.listboxik.insert(END, i[0])  # добавляет значение i(1) (название сертификата) в листбокс


        # 3 кнопки для выбора компании выдавшей сертификат
        crtfcts = StringVar()
        crtfcts.set("")
        colum = 0
        organisatione = ('Cisco', 'Comptia', 'Microsoft')
        self.cert = []

        for i in organisatione:
            crtf = Radiobutton(self, text=i, variable=crtfcts, value=i, command=naznacheniye_cert)
            crtf.grid(row=23, column=colum, sticky=W)
            colum += 1

        def del_curs():
            '''Для стирания курсов'''
            self.listboxik.delete(0, END)



        # Основной выпадающий список сертификатов

        # создание листбокса
        self.listboxik = Listbox(self, selectmode="multiple")
        self.listboxik.grid(row=24, column=0, sticky=W)

        # Сохранение выбранных курсов
        def vibor_certif():
            indexes = self.listboxik.curselection()
            items = []
            for idx in indexes:
                if idx < len(self.cert):
                    entry = self.cert[idx]
                    value = entry[1] if (hasattr(entry, '__getitem__') and len(entry) > 1) else entry
                    items.append(value)
            print(items)  # для теста, потом удалить
            self.ist_sert.delete(0.0, "end")
            self.ist_sert.insert(0.0, str(items))
            self.selected_certif = items
            return items  # выдает списком [], использовать для x-ray


        Button(self, text='Выбрать сертификат для поиска', command=vibor_certif
               ).grid(row=24, column=1)

        #Выбранные сертификаты
        Label(self, text='Выбранные сертификаты')

        self.ist_sert=Text(self, width=20,height=2,wrap=WORD)
        self.ist_sert.grid(row=24,column=2,sticky=W)



        # ФИНАЛ Вывод результата
        Button(self,text='Вывод финального x-ray запроса', command=self.perem_x_ray
               ).grid(row=25,column=0,sticky=W)

        # Текстовое поле для вывода результата
        self.x_rey_text=Text(self, width=75,height=25,wrap=WORD)
        self.x_rey_text.grid(row=25,column=1,columnspan=3)


    def update_text(self):
        #self.x_rey_text.set(None)
        print("этетсэ")

        x_site=self.site.get()
        x_grazhdanstvo = self.flags.get()
        x_gorod= self.gorod,get()

    # Функция для обновления дополнительных навыков
    def update_text_skill(self):
        selected=[label for var, label in self.all_hard_skills if var.get()] #проверить переменные
        self.selected_skill=selected
        print(selected)
        return selected

    # функция для обновления сертификатов
    def update_text_sertif(self):
        if getattr(self, "ist_vars", None):
            s = [v.get() for v in self.ist_vars if v.get()]
        else:
            s = list(getattr(self, "selected_certif", []) or [])
        self.selected_certif = s
        print(s)
        return s



    # Функция для формирования финального X-ray запроса
    def perem_x_ray(self):
        '''Должен собрать все переменные и соединить в текст'''
        # site: self.site AND ("Доктор наук" AND "Системная инженерия") AND ("Москва" OR "Казахстан")
        # AND ("pyrthon" OR "Python") AND "финансы" AND "Сбербанк" AND "Cisco CCIE"
        x_ray_text = ''

        # Сайт
        if self.site.get() != None:
            x_ray_text += 'site:'
            x_ray_text += self.site.get()

        # Вывод стран
        if self.selected != None:
            sel=''
            for i in self.selected:
                for y in i:
                    sel = sel + y + ' AND '
            x_ray_text += ' AND ' + sel

        # Образование
        if self.obr_sre.get() != False:
            x_ray_text += 'middle'
        if self.obr_bach.get() != False:
            x_ray_text += 'bachelor'
        if self.obr_mag.get() != False:
            x_ray_text += 'magistratura'
        if self.obr_phd.get() != False:
            x_ray_text += 'phd'

        # Направление обучения
        # ранее можно было бы создать список большой
         # туда все переменные и к ним значения,перебор и
          # постановка значений, но не хочется

        if self.napr_sys_eng.get() != False:
            x_ray_text += ' AND ("Системная инженерия" OR "System Engineering") '
        if self.napr_cy_sec.get() != False:
            x_ray_text += ' AND ("Кибербезопасность" OR "Cybersecurity") '
        if self.napr_dat_sci.get() != False:
            x_ray_text += ' AND ("Data Science" OR "Data Science ") '
        if self.napr_bus_anal.get() != False:
            x_ray_text += ' AND ("Бизнес-аналитика" OR "Business Analytics ") '
        if self.napr_data_anal.get() != False:
            x_ray_text += ' AND ("Аналитика данных" OR "Data Analytics ") '
        if self.napr_b_data_anal.get() != False:
            x_ray_text += ' AND ("Аналитика больших данных" OR "Big Data Analytics ") '
        if self.napr_dat_eng.get() != False:
            x_ray_text += ' AND ("Инженерия данных" OR "Data Engineering ") '
        if self.napr_mach_learn.get() != False:
            x_ray_text += ' AND ("Машинное обучение" OR "Machine Learning ") '
        if self.napr_deep_learn.get() != False:
            x_ray_text += ' AND ("Глубокое обучение" OR "Deep Learning ") '
        if self.napr_nat_lang_proc.get() != False:
            x_ray_text += ' AND ("Обработка естественного языка" OR "Natural Language Processing ") '

        # Спецализация кандидата для поиска
        if self.prof.get() != "":
            x_ray_text += 'AND ' + self.prof.get()

        # Уровень квалификации
        if self.opit.get() != "":
            x_ray_text += ' AND ' + self.opit.get()

        # Вакансии и навыки
        select=self.update_text_skill()
        if select != "":
            for i in select:
                x_ray_text += ' AND ' + i

        # Дополнительный навык
        if self.kart != '':
            for i in self.kart:
                x_ray_text += ' AND ' + i

        # Сферы предыдущей работы
        if self.sfera.get() != "":
            x_ray_text += ' AND ' + self.sfera.get()

        # Предыдущий проект
        if self.comp != '':
            for i in self.comp:
                x_ray_text += ' AND ' + i

        # Сертификаты
        s = self.update_text_sertif() # должен быть аналог self.update_text_skill()
        if s != "":
            for i in s:
                x_ray_text += ' AND ' + str(i)
        print(str('авав'))

        # ФИНАЛ, выдача x-ray запроса пользователю
        #self.x_rey_text=(x_ray_text)
        self.x_rey_text.insert(1.0,x_ray_text )
        print(x_ray_text)  # для теста















        # x_ray_text = ()
        #'site:'+ self.site.get() + ' AND ' + sel + ' AND '+ self.gorod.get() + ' AND '+ self.obr_sre.get() + self.obr_bach.get(),
        #self.obr_mag.get())
        print(x_ray_text) #для теста














        # транслитерация для всего необходимого
        #def Translit(self,text):
            #keys_list=list(TRANSLITERATION.keys())
            #text=self.gorod

        #for i in TRANSLITERATION: #in self.gorod ?
            #if i in keys_list:
                # берем номер буквы в транслитератион
                #position= keys_list.index(i)
                 # номер буквы и 2 позиция вставляем в новое слово
                #new_text = ""
                #new_text += TRANSLITERATION[position]
                # возможно тут должно быть: TRANSLITERATION[keys_list[position]]
            #else:
                #print('код не работает')
        #print ('Тест, транслитерации',new_text)
        #self.gorod += new_text # не уверен что так работает



root = Tk() # Окно
root.geometry("900x700")
root.title("x-ray запросы") # Название окна
app = Applicatione(root)
root.mainloop()





































