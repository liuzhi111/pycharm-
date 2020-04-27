import numpy as np


def logp_trace(model):
    """
    return a trace of logp for model
    """
    # init
    db = model.db
    n_samples = db.trace('deviance').length()
    logp = np.empty(n_samples, np.double)
    # loop over all samples
    for i_sample in range(n_samples):
        # set the value of all stochastic to their 'i_sample' value
        for stochastic in model.stochastics:
            try:
                value = db.trace(stochastic.__name__)[i_sample]
                stochastic.value = value

            except KeyError:
                print("No trace available for %s. " % stochastic.__name__)

        # get logp
        logp[i_sample] = model.logp
    return logp


# 计算平均学分绩点
def compute_gpa(grades, points={'A+':4.0, 'A':4.0, 'A-':3.67,
                                'B+':3.33,'B':3.0,'B-':2.67,
                                'C+':2.33,'C':2.0,'C-':1.67,
                                'D+':1.33,'D':1.0,'F':0.0}):
    num_courses = 0
    total_points = 0
    for i in grades:
        if g in points:
            num_courses += 1
            total_points += points[g]
    return  total_points / num_courses


def is_multiple(n,m):
    try:
        if isinstance(n, int) & isinstance(m,int):
            print("a is int")
    except ValueError:
        print('输入的参数不是整型')
    if n % m == 0:
        print('n is the m beishu').format(n,m)
        return True
    else:
        print('n is not the m beishu').format(n,m)
        return False



if __name__ == '__main__':
    print(is_multiple(17.1,2))
