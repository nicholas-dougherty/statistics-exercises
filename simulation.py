#   ▄████████  ▄█    ▄▄▄▄███▄▄▄▄   ███    █▄   ▄█          ▄████████     ███      ▄█   ▄██████▄  ███▄▄▄▄  # 
#  ███    ███ ███  ▄██▀▀▀███▀▀▀██▄ ███    ███ ███         ███    ███ ▀█████████▄ ███  ███    ███ ███▀▀▀██▄# 
#  ███    █▀  ███▌ ███   ███   ███ ███    ███ ███         ███    ███    ▀███▀▀██ ███▌ ███    ███ ███   ███# 
#  ███        ███▌ ███   ███   ███ ███    ███ ███         ███    ███     ███   ▀ ███▌ ███    ███ ███   ███# 
#▀███████████ ███▌ ███   ███   ███ ███    ███ ███       ▀███████████     ███     ███▌ ███    ███ ███   ███# 
#         ███ ███  ███   ███   ███ ███    ███ ███         ███    ███     ███     ███  ███    ███ ███   ███# 
#   ▄█    ███ ███  ███   ███   ███ ███    ███ ███▌    ▄   ███    ███     ███     ███  ███    ███ ███   ███# 
# ▄████████▀  █▀    ▀█   ███   █▀  ████████▀  █████▄▄██   ███    █▀     ▄████▀   █▀    ▀██████▀   ▀█   █▀ # 
#                                             ▀                                                           # 
#|-------------------------------------------------------------------------------------------------------|#
# necessary imports
import numpy as np
import pandas as pd
# for reproducibility
np.random.seed(124)
#|-------------------------------------------------------------------------------------------------------|#
# 1. How likely is it that you roll doubles when rolling two dice?
# There are many ways to solve this
die_1 = np.random.choice([1, 2, 3, 4, 5, 6], size = 10_000)
die_2 = np.random.choice([1, 2, 3, 4, 5, 6], size = 10_000)

(die_1 == die_2).mean()
#  returns p of 0.164
# -----------------------------------------------------------------
# or
n_trials = nrows = 10_000
n_dice = ncols= 2

# possible outcomes for each roll
rolls = np.random.choice([1,2,3,4,5,6], n_trials * n_dice).reshape(nrows, ncols)

# assign to a df and use lambda to check for doubles 
df = pd.DataFrame(rolls).apply(lambda x : x[0] == x[1] in x.values, axis=1)

# gives the probability of rolling doubles >> 0.163
df.mean()
# ----------------------------------------------------------------
# or 
outcomes = [1,2,3,4,5,6]
n_rows = 1_000_000 # 1 million trials
n_cols = 2
rolls = np.random.choice(outcomes, size = (n_rows,n_cols))

# use a list comprehension: 
# a list of the length of the uniques for each instance for the full number of simulations by index,
# but only if the number of uniques is 1
doubles = [len(np.unique(rolls[n])) for n in range(0, n_rows-1) if len(np.unique(rolls[n])) ==1]

len(doubles) # number of times we rolled doubles
prob_doubles = len(doubles)/len(rolls)
# returns p of 0.166672
#|-------------------------------------------------------------------------------------------------------|#
#|-------------------------------------------------------------------------------------------------------|#
# 2. If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

coin_outcomes = [1, 0]
n_simulations = 100_000
n_trials = 8 
flips = np.random.choice(coin_outcomes, size = (n_simulations,n_trials))
count_heads = flips.sum(axis = 1)

p_exactly_3heads = (count_heads == 3).mean()
p_morethan_3heads = (count_heads > 3).mean()

# returns p exactly 3 heads of 0.21741
# returns p more than 3 heads of 0.63873
#|-------------------------------------------------------------------------------------------------------|#
#|-------------------------------------------------------------------------------------------------------|#
# 3. There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup.
#    Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two
#    billboards I drive past both have data science students on them?
#
#               Three Web Dev cohorts for every 1 Data Science cohort, which is a ratio of 3:1,
#           or think of it this way:
#           each sign is a biased coin flip, where we know we have a 1 out of 4 chance
#           of getting a data science student.
#           theoretical prob both boards have ds student: (1/4) * (1/4) = 0.0625
n_simulations = n_rows = 10 ** 6
n_cols = 2
prob_ds = 0.25 #1 out 4 prob that a ds student on billboard
data = np.random.random((n_rows, n_cols))
((data < prob_ds).sum(axis =1) == 2).mean()
# returns p of 0.062627
#|-------------------------------------------------------------------------------------------------------|#
#|-------------------------------------------------------------------------------------------------------|#
# 4. Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. 
#    If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to
#    buy some poptarts on Friday afternoon?
#
mu, sigma = 3, 1.5 #mean and std deviation
n_rows = 10_0000
n_cols = 5 
consumed = np.random.normal(mu, sigma, size=(n_rows, n_cols))
pops_bought = consumed.sum(axis =1)
poptarts_on_fri = 17 - pops_bought
(poptarts_on_fri >= 1).mean()
# returns p of 0.6204
#|-------------------------------------------------------------------------------------------------------|#
#|-------------------------------------------------------------------------------------------------------|#
# 5. Compare Heights
#                    Men have an average height of 178 cm and standard deviation of 8cm.
#                    Women have a mean of 170, sd = 6cm.
#                    If a man and woman are chosen at random, P(woman taller than man)?

# heights of men chosen at random
mu_men, sigma_men = 178, 8
men = np.random.normal(mu_men, sigma_men, size=(10_000, 1))

# heights of randomly chosen women
mu_women, sigma_women = 170, 6
women = np.random.normal(mu_women, sigma, size=(10_000, 1))

prob_woman_taller = (women > men).mean()
# returns p of 0.2131
#|-------------------------------------------------------------------------------------------------------|#
#|-------------------------------------------------------------------------------------------------------|#
# 6. When installing anaconda on a student's computer, there's a 1 in 250 chance that the download
#.   is corrupted and the installation fails. What are the odds that after having 50 students download 
#    anaconda, no one has an installation issue? 

p_fail = 0.004
p_success = 0.996
n_cols = 50 # number of students installing anaconda
n_rows = 10_000
trials = np.random.random((n_rows, n_cols))
successful_install = trials < p_success
(successful_install.sum(axis=1)== 50).mean()
# returns p of 0.8168
#|-------------------------------------------------------------------------------------------------------|#
# What are the odds that after having 100 students download anaconda, no one has an installation issue?
p_fail = 0.004
p_success = 0.996
n_cols = 100
n_rows = 10_000
trials = np.random.random((n_rows, n_cols))
successful_install = trials < p_success
(successful_install.sum(axis=1)== 100).mean()
# returns p of 0.6707
#|-------------------------------------------------------------------------------------------------------|#
# What is the probability that we observe an installation issue within the first 150 students that download anaconda?
p_fail = 0.004
p_success = 0.996
n_cols = 150
n_rows = 10_000
trials = np.random.random((n_rows, n_cols))
failed_install = trials < p_fail
(failed_install.sum(axis=1) > 0).mean()
# returns p of 0.4517
#|-------------------------------------------------------------------------------------------------------|#
# How likely is it that 450 students all download anaconda without an issue?
p_fail = 0.004
p_success = 0.996
n_cols = 450
n_rows = 10_000
trials = np.random.random((n_rows, n_cols))
success_install = trials < p_success
(success_install.sum(axis=1) == 450).mean()
#  returns p  of 0.1657
#|-------------------------------------------------------------------------------------------------------|#
#|-------------------------------------------------------------------------------------------------------|#
# 7. There's a 70% chance on any given day that there will be at least one food truck at Travis Park. 
# However, you haven't seen a food truck there in 3 days. How unlikely is this?
n_cols = 3
n_rows = 10 ** 6
outcomes = [0,1]
# treating as independent events
p_truck = 0.7
p_notruck = 0.3
data = np.random.choice(outcomes, n_rows * n_cols, p = [p_notruck,p_truck]).reshape(n_rows, n_cols)
(data.sum(axis = 1)==0).mean()
# returns p of 0.027402
#|-------------------------------------------------------------------------------------------------------|#
#  or with df
(pd.DataFrame(data).apply(lambda row: 1 not in row.values, axis =1)).mean()
# returns p of 0.027402
#|-------------------------------------------------------------------------------------------------------|#
# How likely is it that a food truck will show up sometime this week?
n_cols = 7
n_rows = 10 ** 6
outcomes = [0,1]
p_truck = 0.7
p_notruck = 0.3
data = np.random.choice(outcomes, n_rows * n_cols, p = [p_notruck, p_truck]).reshape(n_rows, n_cols)
(data.sum(axis = 1)>0).mean()
# returns p of 0.972958
#|-------------------------------------------------------------------------------------------------------|#
#|-------------------------------------------------------------------------------------------------------|#
# 8. If 23 people are in the same room, what are the odds that two of them share a birthday?  

#               365 days a year
#               23 people in the room
#               we want an instance where both days are the same number

# not including those born on leap days
outcomes = range(0,365)
n_trials = 23
n_simulations = 1_000_000

# Let's get our simulations. We'll make a simulation of 1 million classrooms of 23 students.

# outcomes: possible unique days of the year that a person could have.
# n_simulations: the number of simulated classroom trials
# n_trials: the number of student birthdays

classrooms = np.random.choice(outcomes, size = (n_simulations, n_trials))

# when len(np.unique() == 22) we have a situation where 2 people have
# the same bday so that bday is not unique

# using list comprehension
# a list of the length of the uniques for each instance for the full number of simulations by index, 
# but only if the number of uniques is less than the number of students in the class

list_twin_bdays =  [len(np.unique(classrooms[n])) for n in range(0, n_simulations - 1) if len(np.unique(classrooms[n])) < 23]

# length of list of twin bdays is the number of times we had a class with shared bdays, 
# divide that by total simulations
prop_twins = len(list_twin_bdays) / n_simulations
#  returns p of 0.507675
#|-------------------------------------------------------------------------------------------------------|#

# What if it's 20 people?
outcomes = range(0,365)
n_trials = 20
n_simulations = 1_000_000

classrooms = np.random.choice(outcomes, size = (n_simulations, n_trials))
list_twin_bdays =  [len(np.unique(classrooms[n])) for n in range(0, n_simulations - 1) if len(np.unique(classrooms[n])) < 20]
prop_twins = len(list_twin_bdays) / n_simulations
# returns p of 0.411709
#|-------------------------------------------------------------------------------------------------------|#

# What if it's 40 people?
outcomes = range(0,365)
n_trials = 40
n_simulations = 1_000_000

classrooms = np.random.choice(outcomes, size = (n_simulations, n_trials))
list_twin_bdays =  [len(np.unique(classrooms[n])) for n in range(0, n_simulations - 1) if len(np.unique(classrooms[n])) < 40]
prop_twins = len(list_twin_bdays) / n_simulations
#  returns p of 0.891755
#|-------------------------------------------------------------------------------------------------------|#
#|-------------------------------------------------------------------------------------------------------|#
#        ▄▀▀▀█▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀█▄▄▄▄     ▄▀▀▄ ▄▀▄  ▄▀▀█▄   ▄▀▀▀█▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▀▄   ▄▀▀▄  ▄▀▄        #
#       █    █  ▐ █  █   ▄▀ ▐  ▄▀   ▐    █  █ ▀  █ ▐ ▄▀ ▀▄ █    █  ▐ █   █   █ █   █  █ █    █   █        #
#       ▐   █     ▐  █▄▄▄█    █▄▄▄▄▄     ▐  █    █   █▄▄▄█ ▐   █     ▐  █▀▀█▀  ▐   █  ▐ ▐     ▀▄▀         #
#          █         █   █    █    ▌       █    █   ▄▀   █    █       ▄▀    █      █         ▄▀ █         #
#        ▄▀         ▄▀  ▄▀   ▄▀▄▄▄▄      ▄▀   ▄▀   █   ▄▀   ▄▀       █     █    ▄▀▀▀▀▀▄     █  ▄▀         #
#       █          █   █     █    ▐      █    █    ▐   ▐   █         ▐     ▐   █       █  ▄▀  ▄▀          #
#       ▐          ▐   ▐     ▐           ▐    ▐            ▐                   ▐       ▐ █    ▐           #
#                                                                                          Simulation FIN #