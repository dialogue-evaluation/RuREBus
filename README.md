# RuREBus
(описание на русском доступно во второй части readme)

We cordially invite you to participate in the RuREBus (Russian Relation Extraction for Business) shared task. The overall goal of the shared task is to develop business-oriented models capable of relation and/or fact extraction from texts.

## Important dates
* **26.12.2019** -- a [sample of annotated documents](https://github.com/dialogue-evaluation/RuREBus/tree/master/examples) and [markup guidelines](https://github.com/dialogue-evaluation/RuREBus/blob/master/markup_instruction.pdf) are released
* **31.01.2020** --  [first part of the train set](https://github.com/dialogue-evaluation/RuREBus/tree/master/train_data), [evaluation scripts](https://github.com/dialogue-evaluation/RuREBus/tree/master/eval_scripts) and [the unannotated corpus](https://yadi.sk/d/9uKbo3p0ghdNpQ) are released
* **04.02.2020** -- [second part of the train set](https://github.com/dialogue-evaluation/RuREBus/blob/master/train_data/train_part_2.zip)  is released
* **18.02.2020** -- [third part of the train set](https://github.com/dialogue-evaluation/RuREBus/blob/master/train_data/train_part_3.zip) is released
* **20.02.2020** -- [the test set](https://github.com/dialogue-evaluation/RuREBus/tree/master/test_data) is released, the first evaluation phase (for tasks 1 and 3) starts [on codalab](https://competitions.codalab.org/competitions/23407?secret_key=5cf6d204-0f1c-468a-8254-42a2f22ac39a)
* **2.03.2020** -- the submission deadline for systems solving tasks 1 and 3
* **3.03.2020** -- second evaluation phase starts (for task 2) [on codalab](https://competitions.codalab.org/competitions/23407?secret_key=5cf6d204-0f1c-468a-8254-42a2f22ac39a). [NER markup for test set](https://github.com/dialogue-evaluation/RuREBus/blob/master/test_data/test_ner_only.zip) is released.
* **6.03.2020** -- the submission deadline for systems solving task 2
* **7.03.2020** -- the results are announced 
* **We are here*
* **18.03.2020** -- paper submission deadline

## Results

|   *      | NER | RE with NEs | End-to-end RE |
| :---:   | :---:    | :---:    | :---:   |
| **_Team_**   | **_f-measure_** | **_f-measure_** |  **_f-measure_**  |
| **davletov-aa** | **0.560** | 0.369 | |
| **Sdernal** | 0.464 | **0.441** | |
| **ksmith** | 0.463 | 0.152 | **0.062** |
| **viby** | 0.412 | 0.218 |  |
| **dimsolo** | 0.400 | | |
| **bond005** | 0.338 | 0.045 | |
| **Student2020** | 0.253 | | |

*Table is sorted by NER scores, but all 3 tasks are equally important.

Results submitted after the deadline but before the test corpus was published:
|         | NER | RE with NEs | End-to-end RE |
| :---:   | :---:    | :---:    | :---:   |
| **_Team_**   | **_f-measure_** | **_f-measure_** |  **_f-measure_**  |
| **davletov-aa** | 0.561 |  | 0.132 |
| **bondarenko** | 0.498 |  | 0.000 |

## Submission format

### Phase 1.
For phase 1 the submission format is as follows: zip archive containing 2 folders named "set_1" and "set_3". Each folder should contain data for tasks 1 and 3 respectively. 

Date format in each is the same as in [train set](https://github.com/dialogue-evaluation/RuREBus/tree/master/train_data) i. e. for every text there should be .ann file containing BRAT markup of the text (.txt file for each text with text itself is optional). The name of each .ann file should be the same as the name of .txt file from [test set](https://github.com/dialogue-evaluation/RuREBus/tree/master/test_data) provided by organizers

### Phase 2.
For phase 2 the submission format is as follows: zip archive containing 1 folders named "set_2". This folder should contain data for task 2.
Date format is the same as in [train set](https://github.com/dialogue-evaluation/RuREBus/tree/master/train_data) i. e. for every text there should be .ann file containing BRAT markup of the text (.txt file for each text with text itself is optional).
The name of each .ann file should be the same as the name of .txt file from [test set](https://github.com/dialogue-evaluation/RuREBus/tree/master/test_data) provided by organizers.

## Our Motivation
A lot of business applications require relation extraction. Although there are a few corpora, that contain texts annotated with relations, all of them are more of an academic nature and differ from typical business applications. There are a few reasons for this.

First, the annotations are quite tight, i.e. almost every sentence contains an annotated relation. In contrast, the business-oriented documents often contain much less annotated examples. There might be one or two annotated examples in the whole document. Second, the existing corpora cover everyday topics (family relationships, birth and death relations, purchase and sale relations, etc). The business applications require other domain-specific relations. 

The goal of the task is to compare the methods for relation extraction in a more close-to-practice way. For these reasons, we suggest using the documents, produced by the Ministry of Economic Development of the Russian Federation.

The corpus contains regional reports and strategic plans. A part of the corpus is annotated with named entities (8 classes) and semantic relations (11 classes). In total there are approximately 300 annotated documents. The annotation schema and the guidelines for annotators can be found in [here](https://github.com/dialogue-evaluation/RuREBus/blob/master/markup_instruction.pdf) (in Russian).

## Tasks
1. Named entity recognition. The task is evaluated with micro F-measure on named entity spans. 

2. Relation extraction. In this task, the participants will be provided with manually annotated named entities. The task is to extract relations between them. The task is evaluated with micro F-measure.

3. End-to-end relation extraction. The participants have to extract both named entities and the relations between them. The task is evaluated with micro F-measure.

Evaluation scripts are avaliable [here](https://github.com/dialogue-evaluation/RuREBus/tree/master/eval_scripts)

## Dataset 
The dataset consists of:

1. A train set with manually annotated named entities and relations. First and second parts of train set are avaliable [here](https://github.com/dialogue-evaluation/RuREBus/tree/master/train_data)

2.  A large corpus (approx. 280 million tokens) of raw free-form documents, produced by the Ministry of Economic Development. These documents come from the same domain as the train and the test set. This data is avaliable [here](https://yadi.sk/d/9uKbo3p0ghdNpQ).

3. A test set without any annotations

The participants are allowed to annotate additional documents on their own. When solving a business case it can sometimes be more reasonable to spend time enlarging train set rather than tuning model. While it is not always the case participants are welcome to try this strategy. If they decide to do so, they are asked to inform the organizing committee in advance and share the annotated documents. 

## Organizing committee

Ivan Smurov, Vitaly Ivanin, ABBYY: ivan.smurov@abbyy.com, vitalii.ivanin@abbyy.com

Elena Tutubalina, Kazan Federal University: tlenusik@gmail.com

Vladimir Ivanov, Innopolis: nomemm@gmail.com

Veronika Sarkisyan, Ekaterina Artemova, Higher School of Economics: impecopeco@gmail.com, Echernyak@hse.ru

Anton Emelyanov, Sberbank: login-const@mail.ru

Tatiana Batura, Novosibirsk State University: tatiana.v.batura@gmail.com

To get RuREBus updates please join [our telegram channel](https://t.me/RuREBus). We will be happy to answer any questions about the shared task in [our telegram chat](https://t.me/joinchat/GH1hLBH6dv8tTviF-dBFLA). 


# RuREBus
Приглашаем принять участие в **RuREBus** (Russian Relation Extraction for Business) – соревновании по извлечению отношений(фактов) в постановке, приближенной к индустриальным задачам.

## Мотивация:
Извлечение отношений – одна из самых востребованных бизнесом задач. Существует несколько стандартных корпусов для задачи извлечения отношений на английском языке. Однако, все они достаточно далеки от типичной бизнес-постановки задачи по следующим причинам. 

Во-первых, отношения выделены в тексте достаточно плотно (напротив, в бизнес-задачах часто есть 1-2 вхождения отношений на достаточно объемные тексты). Во-вторых, в стандартных корпусах определены отношения бытового и повседневного характера (отношение работы персоны в компании, купли/продажи, владения, родственные отношения, факты рождения и смерти и т. п.), тогда, как в бизнес-задачах обычно требуется выделять отношения, имеющие специфическую природу, связанную с тематикой предметной области.

Целью дорожки является сравнение методов извлечения отношений на русском языке в постановке, приближенной к практике. Для этого предлагается использовать корпус Минэкономразвития (МЭР) (около 280 млн. токенов). 

Корпус представляет собой различные отчеты региональных органов о проделанной работе и запланированных мероприятиях, а также прогнозы и планы на будущее. Некоторое подмножество корпуса будет размечено специальными именованными сущностями (8 классов) и семантическими отношениями на них (11 классов). Всего хотелось бы получить как минимум несколько сотен размеченных текстов.


Эскиз инструкции для разметчиков можно прочесть [здесь](https://github.com/dialogue-evaluation/RuREBus/blob/master/markup_instruction.pdf)
 (мелкие детали могут уточняться). 

## Задачи:
Соревнование будет проводиться по трем задачам: 

1. Выделение именованных сущностей (named entity recognition, NER). Метрика оценивания - микро F-мера с точным совпадением спана сущности.

2. Извлечение семантических отношений между сущностями (relation extraction, RE). В данной задаче заранее сущности заданы в тексте и требуется установить отношения между ними. Метрика оценивания -- микро F-мера.

3. End-to-end извлечение семантических отношений. В данной задаче заранее сущности не заданы, требуется выделить сущности и отношения между ними. Метрика совпадает с п. 2.

Скрипты для оценки качества доступны [здесь](https://github.com/dialogue-evaluation/RuREBus/tree/master/eval_scripts)

## Данные:

Участникам будут выданы следующие файлы: 

(i) Обучающая выборка, размеченная вручную сущностями и отношениями; первая часть обучающей выборки доступна [здесь](https://github.com/dialogue-evaluation/RuREBus/tree/master/train_data)

(ii) Большая (порядка 280 миллионов токенов) неразмеченная коллекция текстов МЭР (что, опять же, приближает нас к бизнес-постановке, когда неразмеченные тексты зачастую есть в изобилии). Коллекция неразмеченных текстов доступна [здесь](https://yadi.sk/d/9uKbo3p0ghdNpQ).

(iii) Тестовая выборка. Оценка качества автоматических моделей будет происходить на тестовой выборке. 

 
Важно отметить, что оргкомитет принципиально не будет запрещать участникам самим размечать дополнительные тексты. Дорожка позиционируется как симуляция реальной рабочей задачи, и, если для улучшения решения задачи эффективнее потратить время на разметку текстов, а не на улучшение модели, размечать тексты – валидная стратегия. Если участники прибегнут к дополнительной разметке, они будут должны предупредить оргкомитет и прислать размеченные ими тексты.


Дополнительный смысл выдачи участникам большого корпуса неразмеченных текстов из одной и той же предметной области основан на следующем предположении: мы хотим позволить участникам дорожки самостоятельно предобучить языковые модели на неразмеченных данных. 
Мы хотим проверить гипотезу: верно ли, что такие языковые модели будут показывать лучшие результаты, по сравнению с моделями, предобученными на текстах из других предметных областей.

## Важные даты:
* **26 декабря 2019** - [выдача примера размеченных данных](https://github.com/dialogue-evaluation/RuREBus/tree/master/examples) и [инструкции для разметки](https://github.com/dialogue-evaluation/RuREBus/blob/master/markup_instruction.pdf)
* **31 января 2020** - выдача [первой части собучающей выборки](https://github.com/dialogue-evaluation/RuREBus/tree/master/train_data), [скриптов для оценки качества](https://github.com/dialogue-evaluation/RuREBus/tree/master/eval_scripts) и [всего неразмеченного корпуса](https://yadi.sk/d/9uKbo3p0ghdNpQ)
* **4 февраля 2020** - выдача [второй части обучающей выборки](https://github.com/dialogue-evaluation/RuREBus/blob/master/train_data/train_part_2.zip)
* **18 февраля 2020** - выдача [третьей части обучающей выборки](https://github.com/dialogue-evaluation/RuREBus/blob/master/train_data/train_part_3.zip)
* **20 февраля 2020** - выдача [тестовой выборки](https://github.com/dialogue-evaluation/RuREBus/tree/master/test_data) начало первой фазы тестирования (для задач 1 и 3) [в codalab](https://competitions.codalab.org/competitions/23407?secret_key=5cf6d204-0f1c-468a-8254-42a2f22ac39a)
* **2 марта 2020** - финальная подача систем для задач 1 и 3
* **3 марта 2020**  - начало второй фазы тестирования (для задачи 2) [в codalab](https://competitions.codalab.org/competitions/23407?secret_key=5cf6d204-0f1c-468a-8254-42a2f22ac39a). Опубликована [разметка NER тестовых данных](https://github.com/dialogue-evaluation/RuREBus/blob/master/test_data/test_ner_only.zip) for test is released.
* **6 марта 2020** - финальная подача систем для задачи 2
* **7 марта 2020** - объявление официальных результатов
* **Вы находитесь здесь**
* **18 марта 2020** - дедлайн по статьям в сборник конференции Dialogue-2020

## Результаты соревнования

|   *      | NER | RE with NEs | End-to-end RE |
| :---:   | :---:    | :---:    | :---:   |
| **_Team_**   | **_f-measure_** | **_f-measure_** |  **_f-measure_**  |
| **davletov-aa** | **0.560** | 0.369 | |
| **Sdernal** | 0.464 | **0.441** | |
| **ksmith** | 0.463 | 0.152 | **0.062** |
| **viby** | 0.412 | 0.218 |  |
| **dimsolo** | 0.400 | | |
| **bond005** | 0.338 | 0.045 | |
| **Student2020** | 0.253 | | |

*Таблица отсортирована по результатам первой дорожки, однако значимость всех трех дорожек одинакова.

Результаты, опубликованные после дедлайна (но до публикации тестовой выборки):

Results submitted after the deadline but before the test corpus was published:
|         | NER | RE with NEs | End-to-end RE |
| :---:   | :---:    | :---:    | :---:   |
| **_Team_**   | **_f-measure_** | **_f-measure_** |  **_f-measure_**  |
| **davletov-aa** | 0.561 |  | 0.132 |
| **bondarenko** | 0.498 |  | 0.000 |

## Формат сабмита

### Первая фаза.
Сабмит для первой фазы должен иметь следующий вид: zip-архив с 2 папками - "set_1" и "set_3", содержащими данные для первой и третьей задачи соответственно. 

Формат данных в каждой папке такой же как для [обучающей выборки](https://github.com/dialogue-evaluation/RuREBus/tree/master/train_data) т. е. для каждого текста должен иметься в наличии .ann файл, содержащий аннотацию текста в формате BRAT (включение .txt файлов опционально). Имя каждого .ann файла должно совпадать с именем .txt файла из [тестовой выборки](https://github.com/dialogue-evaluation/RuREBus/tree/master/test_data), предоставленной организаторами.

### Вторая фаза.
Сабмит для второй фазы должен иметь следующий вид: zip-архив с 1 папкой - "set_2", содержащий данные для второй задачи.

Формат данных в папке такой же как для [обучающей выборки](https://github.com/dialogue-evaluation/RuREBus/tree/master/train_data) т. е. для каждого текста должен иметься в наличии .ann файл, содержащий аннотацию текста в формате BRAT (включение .txt файлов опционально). Имя каждого .ann файла должно совпадать с именем .txt файла из [тестовой выборки](https://github.com/dialogue-evaluation/RuREBus/tree/master/test_data), предоставленной организаторами.


## Состав оргкомитета и контакты

Иван Смуров, Виталий Иванин, ABBYY: ivan.smurov@abbyy.com, vitalii.ivanin@abbyy.com

Елена Тутубалина, Казанский федеральный университет: tlenusik@gmail.com

Владимир Иванов, Иннополис: nomemm@gmail.com

Вероника Саркисян, Екатерина Артемова  / НУЛ ММВП, НИУ ВШЭ: impecopeco@gmail.com, Echernyak@hse.ru

Антон Емельянов, ПАО Сбербанк: login-const@mail.ru

Татьяна Батура, Новосибирский Государственный Университет: tatiana.v.batura@gmail.com

Объявления о ходе соревнования будут делаться в [нашем телеграм-канале](https://t.me/RuREBus). Все вопросы о соревновании можно задать в [наш чат в телеграме](https://t.me/joinchat/GH1hLBH6dv8tTviF-dBFLA). 
