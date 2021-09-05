# collaborative-filtering
Simple Collaborative filtering (CF) model based on Pearson correlation and result ranking. Correlation is determined by preferences matching and ratings.

## [RU] Описание работы алгоритма на примере рекомендации маршрута:
Шаг 1. Рассчитывается коэффициент подобия пользователей. В качестве него используется коэффициент корреляции Пирсона. Параметрами служат маршруты пользователя с поставленными оценками 
по пятибалльной шкале.

Шаг 2. После поиска подобных пользователей осуществляется ранжирование и выбор наиболее подходящих по коэффициенту пользователей.

Шаг 3. Составляется таблица с подходящими пользователями, содержащая маршруты из их списков, которых нет у исходного пользователя, а также их оценки.

Шаг 4. По каждому маршруту производится умножение коэффициента подобия пользователя на оценку, поставленную им.

Шаг 5. Вычисляется сумма коэффициентов подобия всех пользователей, а также сумма показателей 4 шага.

Шаг 6. Вычисляется прогнозируемая оценка пользователя: итоговая сумма показателей делится на сумму коэффициентов подобия по каждому маршруту.

Шаг 7. Маршруты ранжируются по наиболее высокой прогнозируемой оценке для показа рекомендации.
