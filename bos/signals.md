# Сервисы, сигналы

### Рассматриваемые вопросы
1. Сервисы и их роль в ОС Linux
2. Process identifier
3. Сигналы как средство управления процессами

### Термины, которые нужно усвоить
1. systemctl
2. pid
3. `ps aux` и поля вывода этой команды

### Отчёт по пз
4 скриншота по соответствующим заданиям :
1. systemctl
2. pid процесса init
3. Результат выполнения kill для своего скрипта
4. "Русская рулетка"

### Теория
**Cервисы**

В операционной системе Linux, так же, как и в Windows, кроме обычных программ, которые могут взаимодействовать с пользователем, есть еще один вид программ. Это работающие в фоне службы, они следят за состоянием системы, обеспечивают автоматическое подключение внешних устройств и сети, позволяют процессам взаимодействовать с оборудованием (dbus), а также в виде служб реализованы различные веб-серверы и серверы баз данных. В отличие от пользовательских программ, службы выполняются в фоне, и пользователь не имеет к ним прямого доступа.

Чтобы всем этим управлять нужна основная служба - система инициализации, которая будет запускать службы linux в нужный момент, следить чтобы они нормально работали, записывать сообщения логов, и самое главное позволять останавливать службы. Раньше, для управления службами использовались скрипты. Можно запустить службу из терминала, раньше, каждая служба запускалась в фоновом режиме одна за другой, без возможности параллельного запуска и возвращала свой PID процесса скрипту инициализации, он сохранялся и потом с помощью этого PID можно было проверить работает ли служба и остановить службу linux если это нужно. Все это можно сделать и вручную.

Но потом на смену этому методу пришла новая модель и система инициализации systemd. Система инициализации запускается сразу после загрузки ядра и начинает инициализировать службы, теперь появилась возможность параллельной инициализации, а также зависимостей между службами. Таким образом, теперь можно определить сложное дерево порядка запуска служб. Но мы не будем вникать в подробности создания служб, нас интересует только сам процесс запуска. После запуска systemd собирает весь вывод службы в лог, и следит за ее работой, если служба аварийно завершилась, то автоматически ее перезапускает.

Существуют такие типы служб:
   * service - обычная служба, программа
   *  target - группа служб
   * automount - точка автоматического монтирования
   *  device - файл устройства, генерируется на этапе загрузки
   *  mount - точка монтирования
   *  path - файл или папка
   *  scope - процесс
   *  slice - группа системных служб systemd
   *  snapshot - сохраненное состояние запущенных служб
   *  socket - сокет для взаимодействия между процессами.



**Process Id**

Каждый процесс в операционной системе имеет свой уникальный идентификатор, по которому можно получить информацию об этом процессе, а также отправить ему управляющий сигнал или завершить.
В Linux такой идентификатор называется **PID** - process id.

Самым первым стартует процесс **init**, его pid равен 1. Расположен по пути /sbin/init. Его назначение состоит в том, чтобы запустить все остальные процессы, рабочее окружение.
В семействе Linux **pid** хранится в переменной целочисленного типа.

**Сигналы**

Сигнал в операционных системах семейства Unix — асинхронное уведомление процесса о каком-либо событии, один из основных способов взаимодействия между процессами. Когда сигнал послан процессу, операционная система прерывает выполнение процесса, при этом, если процесс установил собственный обработчик сигнала, операционная система запускает этот обработчик, передав ему информацию о сигнале, если процесс не установил обработчик, то выполняется обработчик по умолчанию.
Сигналы посылаются:

  * из терминала, нажатием специальных клавиш или комбинаций (например, нажатие Ctrl-C генерирует SIGINT, Ctrl-\ SIGQUIT, а Ctrl-Z SIGTSTP);

  * ядром системы:
      * при возникновении аппаратных исключений (недопустимых инструкций, нарушениях при обращении в память, системных сбоях и т. п.);

      * ошибочных системных вызовах;

      * для информирования о событиях ввода-вывода;
  * одним процессом другому (или самому себе), с помощью системного вызова kill(), в том числе:
      * из shell, утилитой /bin/kill.

Сигналы не могут быть посланы завершившемуся процессу, находящемуся в состоянии «зомби».

**Обработка сигналов**

Обработчик по умолчанию для большинства сигналов завершает выполнение процесса. Для альтернативной обработки всех сигналов, за исключением SIGKILL и SIGSTOP, процесс может назначить свой обработчик или игнорировать их возникновение модификацией своей сигнальной маски. Единственное исключение — процесс с pid 1 (init), который имеет право игнорировать или обрабатывать любые сигналы, включая KILL и STOP

POSIX определяет 28 сигналов, основные из них приведены в таблице:

|Название|Код  | Действие по умолчанию| Описиние
|--|--|--|--|
|Sighup     |1 | Завершение               |Закрытие терминала                                       |
|SIGINT     |2 |Завершение                |Сигнал прерывания (Ctrl+C) из терминала                  |
|SIGQUIT    |3 |Завершение с дампом памяти|Сигнал «Quit» с терминала (Ctrl-\)                       |
|**SIGKILL**|9 |**Завершение**            |**Безусловное завершение**                               |
|SIGSYS     |12|Завершение с дампом памяти|Неправильный системный вызов                             |
|SIGTERM    |15|Завершение                |Сигнал завершения (сигнал по умолчанию для утилиты kill) |
|SIGUSR1    |16|Завершение                |Пользовательский сигнал № 1                              |
|SIGUSR2    |17|Завершение                |Пользовательский сигнал № 2                              |
|SIGTSTP    |20|Остановка процесса        |Сигнал остановки с терминала (Ctrl-Z).                   |
|**SIGSTOP**|23|**Остановка процесса**    |**Остановка выполнения процесса**                        |
|SIGCONT    |25|Продолжить выполнение     |Продолжить выполнение ранее остановленного процесса      |

### Ход работы
1. Здесь мы познакомимся с `systemctl` - инструментом для управления systemd и сервисами.
  Сначала давайте посмотрим запущенные службы linux. Нас будут интересовать только программы, а не дополнительные компоненты, поэтому воспользуемся опцией type:
  `systemctl list-units --type service`

  Команда отобразила все службы, которые известны systemd, они сейчас запущены или были запущены. Программа не пересматривает все файлы, поэтому будут показаны только те службы, к которым уже обращались. Состояние loaded - означает, что конфигурационный файл был успешно загружен, следующая колонка active - служба была запущена, а running или exited значит выполняется ли сейчас служба или она успешно завершила свою работу. Листать список можно кнопками вверх/вниз.

2. Следующая команда позволяет получить список служб linux, в который входят все службы, даже не  запущенные, те, которые не запускались, но известны systemd, но это еще не все службы в системе: `systemctl list-units --type service -all`

  Вы можете отсортировать список служб systemctl по состоянию. Например, только выполняющиеся: `systemctl list-units --type service --state running` Для фильтрации можно брать любой показатель состояния из любой колонки.
  Теперь отфильтруем только службы linux: `systemctl list-unit-files --type service`

  **Сделайте скриншот, на котором видно список запущенных сервисов**

  Чтобы запустить службу используется команда start, например: ` sudo systemctl start application.service`

  Остановить службу linux можно командой: `sudo systemctl stop application`

3. Самый распространённый способ узнать PID - использовать утилиту `ps`:

  `ps aux | grep имя_процесса`, где _имя процесса_ - какой угодно набор символов. Попробуйте заменить это имя на уже известный вам процесс **init**.

  _Обратите внимание_, кроме нужного нам процесса, утилита также выведет PID для grep, ведь процесс был запущен во время поиска. Чтобы его убрать, добавляем такой фильтр:

  `ps aux | grep имя_процесса | grep -v grep`

  **Сделайте скриншот, на котором видно, какой pid имеет процесс init**

4.  Если вам не нужно видеть подробную информацию о процессе, а достаточно только PID, то можно использовать утилиту pgrep:
  `pgrep имя_процесса`. По умолчанию утилита ищет по командной строке запуска процесса, если нужно искать только по имени процесса, то надо указать опцию -f: `pgrep -f имя_процесса`

5. Чтобы посмотреть список доступных сигналов, напишем `kill -l`.

6. Как мы уже выяснили, сигналы служат для взаимодействия с процессами. Давайте попробуем написать простенький bash - скрипт, который наглядно покажет, как именно происходит обработка сигнала.

  Создайте файл `surname.sh`, где surname - Ваша фамилия, в любом удобном месте.

  _Примечание:_ файл можно создать из терминала командой `touch surname.sh`

  Откройте его, вставьте следующий код:

  ```
  #!/bin/bash
  count=0

  trap 'echo; echo "Обработали SIGINT, выходим"; exit 1' SIGINT
  trap 'echo; echo "SIGTERM, засыпаем"; sleep 10' SIGTERM
  while [ $count -lt 100 ]
  do
  		sleep 1
  		(( count++ ))
  		echo $count
  done
  ```

  Не забудьте сделать файл исполняемым - `chmod +x surname.sh`
  После того, как всё готово, разделите окно эмулятора терминала пополам - клик правой кнопкой мыши, split horizontally.

  В верхней части запустите скрипт, в нижней введите `ps aux | grep surname`, после чего, используя полученный PID, напишите kill -15 _pid_, посмотрите за реакцией скрипта.
  Попробуйте нажать Ctrl + C в той части терминала, где выполняется скрипт. Комбинация должна корректно обработаться.

  **Сделайте скриншот, на котором видно, как Вы пишете ps aux, а также видно результат выполнения команды kill и нажатия сочетания клавиш**

7. Теперь попробуем сыграть в русскую рулетку. Создайте файл `roulette.sh`, сделайте его исполняемым. В файл добавьте код:
```
#!/bin/bash
trap 'echo $pid $processname; kill -16 $pid' SIGUSR1
while [[ 1 ]]; do
  process=$(ps aux | shuf -n 1)
  processname=$(echo $process | awk '{print $11}')
  pid=$(echo $process | awk '{print $2}')
  sleep 3
done
```
Этот скрипт определяет случайный процесс, после чего убивает его. Это происходит после отправки ему команды `kill -10 pid`, где _pid_ - process id для запущенного скрипта.

Разделите окно эмулятора терминала на две части, после чего выполняйте команду `kill` до тех пор, пока не доберетесь до важного процесса.

**Сделайте скриншот, на котором видно, как происходит завершение процессов**


### Резюме
В ходе этого ПЗ научиились работать с PID, познакомились с сервисами и вариантами взаимодействия с ними.
