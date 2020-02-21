def endec(range_low, range_hi, num_of_bit, precision):
    decodeds = [];
    num_of_code = 2**num_of_bit;
    unit_range = (range_hi-range_low)/(num_of_code-1);
    for i in range(0,num_of_code):
        decoded = round(range_low+i*unit_range, precision);
        if (decoded > range_hi):
            decoded = range_hi;
        decodeds.append(decoded);
        bin_format_str = '0' + str(num_of_bit) + 'b';
        precision_format_str = '.' + str(precision) + 'f';
        # print(str(format(i,bin_format_str)) + ' ' + str(format(decoded, precision_format_str)));
    return decodeds;

def cal_cost(x, y, precision):
    return round(-11*(x**2)+12*x*y-15*(y**2)-7, precision); # cost function
        
def cal_costs_with_chromosomes(endec,chromosomes,precision): # "chromosomes" means decimal values of binary representation
    costs = [];
    for chromosome in chromosomes:
        x = endec[chromosome[0]];
        y = endec[chromosome[1]];
        costs.append(cal_cost(x,y,precision));
    return costs;

def cal_costs_with_decoded_variables(decoded_variables,precision):
    costs = [];
    for _i in decoded_variables:
        x = _i[0];
        y = _i[1];
        costs.append(cal_cost(x,y,precision));
    return costs;

def cost_weighting(costs, num_of_keep, precision): # input is costs of population and number of survivors
    if (len(costs) <= num_of_keep):
        return None;
    Costs = [];
    Csum = 0;
    for i in range(0,num_of_keep):
        Csum += costs[i];
        
    Pn = [];
    Psum = 0;
    for i in range(0,num_of_keep):
        Costs.append(costs[i]-costs[num_of_keep]);
        Pn.append(Costs[i]/Csum);
        Psum += Pn[i];
    
    Pi = [];
    for i in range(0,num_of_keep):
        temp = 0;
        for j in range(0,i+1):
            temp += Pn[j];
        Pi.append(round(temp/Psum,precision));
    return Pi;

# example #
chromosomes = [[9,2], [4,9], [9,6], [2,5], [2,9], [9,4], [6,9], [5,2]];
# decoded_variables = [[8.6456,-8.9032],[2.0648,19.6136],[5.3552,5.3552],[2.0648, 2.0648]];
# decoded_variables = [[-1.2258,19.6129],
                    # [-8.9032,4.2581],
                    # [7.5484,19.6129],
                    # [-7.8065,-0.1290],
                    # [2.0645,15.2258],
                    # [-1.2258,5.3548],
                    # [5.3548,14.1290],
                    # [-2.3226,2.0645]];
endec = endec(-10,24,5,4);
costs1 = cal_costs_with_chromosomes(endec,chromosomes,4);
print(sorted(costs1));
#costs2 = cal_costs_with_decoded_variables(decoded_variables,4);
Pi = cost_weighting(sorted(costs1),4,4);
print(Pi);
# end of example #