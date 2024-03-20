from scipy.stats import uniform


def generate(size, a=0, b=1):
    scale = b - a
    return uniform.rvs(size=size, loc=a, scale=scale)
