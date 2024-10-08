# AI-System
Лабораторные работы по система ИИ (ИТМО, ПИиКТ-СиППО, 3 курс).

- Студент: `Кобелев Роман Павлович`
- Группа: `P3312`
- ИСУ: `368308`


## Отчет по модулю №1 

- Выбранная предметная область: `Персонажи Dota 2`

---

### Описание целей проекта и его значимости

Данный проект разделяется на две основные цели:

- Создание базы знаний на языке Prolog и онтологии в Protege на основе выбранной предметной области
- Используя готовую базу знаний на языке Prolog, реализовать CLI-приложение, предоставляющее из себя систему
поддержки принятия решений на основе выбранной предметной области

Значимостью данного проекта заключается во __введении в курс искусственного интеллекта__, а также в __базовом
представлении о логических языках программирования__ (относительно императивных и функциональных языков
программирования).

--- 

### Анализ требований

Требования к системе принятия решений:

1) Система должна предоставить пользователю выбрать интересующие его роли, аттрибуты и типы
2) Система должна на основе проведенного с пользователем диалога предоставить ему список подходящих героев
3) Система должна уметь работать с разными базами знаний, созданными на логическом языке Prolog
4) Система должна предоставить пользователю завершить работу программы, не дожидаясь конца диалога, при помощи 
текстовой команды 'exit'

Требования к базе знаний и онтологии:

1) Должны быть представлены герои
2) Должны быть представлены роли, сложность, аттрибуты и типы персонажей
3) У каждой игры должно быть минимум:
   - Один аттрибут
   - Одна роль
   - Один тип
4) У каждого героя должна быть сложность

Примечание: здесь представлены требования по отношению конкретно к самому проекту - основные требования 
можно посмотреть в 
[описании лабораторных работ](https://sunnysubmarines.notion.site/AI-System-a559a46cddc44363bdf27b77e10b7d85). 

--- 

### Изучение основных концепций и инструментов

Сперва стоит разобраться с двумя близкими, но разными понятиями: базой знаний и онтологией.

В информационных источниках много разных мнений насчет того, как отличать базу знаний от онтологии. Мне нравится 
следующая позиция: `Отличие базы знаний и онтологии заключается в исчерпываемости информации о представленной 
предметной области и структурированности данной информации: требования полноте информации к онтологий 
более строгие по сравнению с базой знаний; к тому же онтологии предоставляют структурированную информацию 
(например, в виде классов и соответствующих им свойств), когда базы знаний оперируют лишь множеством фактов и правил;
знаний`

Примечание: я не гарантирую на стопроцентную достоверность данного определения, но оно мне кажется более понятным.

--- 

В качестве одного из инструментов был применен логический язык программирования `Prolog`.
Данный язык оперирует следующими понятиями:

- Факт - в рамках Prolog можно привести аналогию с логическим предикатом (например: факт `use(developer, prolog).`, что 
на математическом языке будет выглядеть `Разработчик использует Prolog`)
- Правило - расширение фактов, которое позволяет нам получать новые знания на основе имеющихся фактов
(например: `hard_skilled_dev(Developer) :- use(Developer, prolog, Ages), Ages > 3.` - Разработчик считается продвинутым 
в случае, если он программирует на Prolog более 3 лет)

К тому же в Prolog константы (они пишутся с малой буквы) и переменные (они, логично, пишутся с большой буквы).

Prolog для поиска решения применяет механизм унификации (если максимально просто говорить - сопоставление с 
базой знаний), на основе которого Prolog подбирает решение и проходится по дереву фактов и правил.

--- 

Основные инструменты для работы с Prolog:

- SWI-Prolog - учебная версия Prolog (содержит консольный интерфейс)
- pyswip - библиотека на Python для работы c Prolog

--- 

### Пример работы системы

```text

    Welcome to the Dota 2 Hero program!
    You will be asked a few questions to find matching heroes.
    Type 'exit' if you want to leave.
    
Enter hero roles you prefer. List of available roles:

- carry
- support
- nuker
- disabler
- durable
- escape
- pusher
- initiator

Enter a message of format: "I prefer roles: <your roles>"
Example: I prefer roles: carry, support

> I prefer roles: durable
Enter hero attributes you prefer. List of available attributes:

- strength
- agility
- intelligence
- universal

Enter a message of format: "I like attributes: <your attributes>"
Example: I like attributes: strength, agility

> I like attributes: agility
Enter hero types you prefer. List of available types:

- melee
- range

Enter a message of format: "I prefer types: <your types>"
Example: I prefer types: melee, range

> a prefer: melee
Invalid input. Please try again.
> I prefer types: melee
Sorry, but there are no matching heroes for your preferences.
```

--- 

### Оценка и интерпретация результатов

Примеры запросов непосредственно к базе знаний в Prolog:

```
hero('Rubick').

hero('Arthas').

hero_attribute('Pudge', Pudge_attribute).

% Найти первого героя нюкера с аттрибутом не сила
hero(Hero), \+(hero_attribute(Hero, strength)), hero_role(Hero, nuker), !.

% Найти героев с аттрибутом сила или универсал, не дальнего боя
findall(Hero, ((hero_attribute(Hero, universal); hero_attribute(Hero, strength)), \+(hero_type(Hero, range))), Result).

% Найти двух героев, которые успешно постоят линию. Но кери должен иметь аттрибут ловкости, а саппорт - интеллект.
findall((Carry, Support), 
    (
        succesful_line(Carry, Support), 
        hero_attribute(Carry, agility),
        hero_attribute(Support, intelligence)
    ), 
    Pairs).
```

Оценка соответствия проекта поставленным требованиям: реализованная система соответствует всем пунктам.

---

### Заключение

Prolog как логический язык программирования предоставляет хорошие возможности реализации систем искусственного проекта, 
а также язык имеет довольно приемлемый порог вхождения (первичная сложность заключается лишь в понимании алгоритма
поиска решения самим Prolog).

## Отчёт по модулю №2

### Лабораторная №1. Метод линейной регрессии 

#### Введение

Написать собственный класс реализации Линейной регрессии для датасета. Подготовить данные и провести предсказание.

#### Описание метода/ Псевдокод метода

Линейные методы предполагают, что между признаками объекта (features) и целевой переменной (target/label) существует линейная зависимость, то есть
$$y = w_1 x_1 + w_2 x_2 + ... + w_k x_k + b, $$ 
где $у$ --- целевая переменная (что мы хотим предсказать), $x_i$ --- признак объекта $х$, $w_i$ --- вес $i$-го признака, $b$ --- bias (смещение, свободный член)

Часто предполагают, что объект $х$ содержит в себе фиктивный признак равный 1 для представления свободного члена $b$. В этом случае формула принимает простой вид:
$y = \langle w, x \rangle,$
где $\langle \cdot, \cdot \rangle$ -- скалярное произведение векторов $w, x \in \mathbb{R}^n$.

Минимизация ошибки по методу наименьших квадратов дает решение:
$$w = (X^TX)^{-1}X^TY$$

#### Результат выполнения

```text
Модель с признаками: longitude, latitude, housing_median_age
Коэффициенты: {'longitude': np.float64(-144631.39545819757), 'latitude': np.float64(-151435.5669793681), 'housing_median_age': np.float64(-1446.0680377662336)}
R^2 score: 0.2321199943747666

Модель с признаками: longitude, latitude, housing_median_age, total_rooms, total_bedrooms
Коэффициенты: {'longitude': np.float64(-142561.02120881825), 'latitude': np.float64(-150187.58851405024), 'housing_median_age': np.float64(6138.173742081696), 'total_rooms': np.float64(83032.71355270591), 'total_bedrooms': np.float64(-69327.3291454719)}
R^2 score: 0.328695109124321

Модель с признаками: longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income
Коэффициенты: {'longitude': np.float64(-87733.46508064512), 'latitude': np.float64(-92801.67298854633), 'housing_median_age': np.float64(14811.300865332723), 'total_rooms': np.float64(-18668.150560301998), 'total_bedrooms': np.float64(50254.706694748034), 'population': np.float64(-43998.153185923955), 'households': np.float64(17220.59295133549), 'median_income': np.float64(77409.30807975867)}
R^2 score: 0.6530725054027173
```

#### Примеры использования метода

1. Прогнозирование продаж:
Компании используют линейную регрессию для прогнозирования будущих продаж на основе исторических данных и других факторов (например, расходов на рекламу). Метод выбран из-за его способности выявлять линейные зависимости между переменными и давать интерпретируемые результаты.

2. Анализ недвижимости:
Оценка стоимости жилья на основе таких факторов, как площадь, расположение, количество комнат. Линейная регрессия эффективна здесь, так как многие факторы, влияющие на цену недвижимости, часто имеют линейную зависимость.

### Лабораторная №2. Метод k-ближайших соседей

#### Введение

Написать собственный класс реализации Линейной регрессии для датасета. Подготовить данные и провести предсказание.

#### Описание метода/ Псевдокод метода

Это один из самых понятных подходов к классификации. На уровне интуиции суть метода такова: посмотри на соседей; какие преобладают --- таков и ты. Формально основой метода является гипотеза компактности: если метрика расстояния между примерами введена достаточно удачно, то схожие примеры гораздо чаще лежат в одном классе, чем в разных.

Для классификации каждого из объектов тестовой выборки необходимо последовательно выполнить следующие операции:

- Вычислить расстояние до каждого из объектов обучающей выборки
- Отобрать объектов обучающей выборки, расстояние до которых минимально
- Класс классифицируемого объекта — это класс, наиболее часто встречающийся среди 
 ближайших соседей

#### Результат выполнения

Результат работы моделей для $k=3, 5, 10$ с разной выборкой признаков.

1. Рандомная выборка

```text
[(3,
  array([[10,  0,  0],
         [ 0, 15,  0],
         [ 0,  0, 11]]),
  np.float64(1.0)),
 (5,
  array([[ 8,  2,  0],
         [ 0, 14,  1],
         [ 0,  0, 11]]),
  np.float64(0.9166666666666666)),
 (10,
  array([[10,  0,  0],
         [ 1, 14,  0],
         [ 0,  0, 11]]),
  np.float64(0.9722222222222222))]
```

2. Фиксированная выборка

```text
[(3,
  array([[10,  1,  0],
         [ 0, 13,  1],
         [ 0,  0, 11]]),
  np.float64(0.9444444444444444)),
 (5,
  array([[ 9,  2,  0],
         [ 0, 14,  0],
         [ 0,  0, 11]]),
  np.float64(0.9444444444444444)),
 (10,
  array([[10,  1,  0],
         [ 0, 14,  0],
         [ 0,  0, 11]]),
  np.float64(0.9722222222222222))]
```

#### Примеры использования метода

1. Рекомендательные системы:
Онлайн-магазины и стриминговые сервисы используют k-NN для рекомендации товаров или контента. Метод выбран, потому что он эффективно находит схожие предпочтения пользователей, основываясь на их предыдущем поведении.
2. Распознавание рукописного текста:
k-NN применяется для классификации рукописных символов. Метод хорошо работает здесь, так как схожие символы обычно имеют схожие характеристики в пространстве признаков.