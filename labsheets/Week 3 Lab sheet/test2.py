def personalAllowance(salary):
  standardAllowance = 11500
  if salary > 100000:
    value = (10000 - standardAllowance)/2
    personalallowance = standardAllowance - value
    return personalallowance
