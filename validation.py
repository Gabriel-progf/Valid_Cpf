def valid_first_digit_cpf(CPF):

    split_cpf = CPF.split('-')
    nums_cpf = split_cpf[0].replace('.', '')

    account_regressive = 10
    tot_sum_multi_numbers = 0

    if nums_cpf is not True:
        for num_str in nums_cpf:
            tot_sum_multi_numbers += int(num_str) * account_regressive
            account_regressive -= 1

    mult_tot_value_per_ten = tot_sum_multi_numbers * 10

    rest_division_per_eleven = mult_tot_value_per_ten % 11

    result_first_digit = 0 if rest_division_per_eleven > 9 else rest_division_per_eleven

    return result_first_digit


def valid_second_digit_cpf(CPF, first_digit):
    split_cpf = CPF.split('-')
    nums_cpf = split_cpf[0].replace('.', '')

    nums_cpf += str(first_digit)

    account_regressive = 11
    tot_sum_multi_numbers = 0

    if nums_cpf is not True:
        for num_str in nums_cpf:
            tot_sum_multi_numbers += int(num_str) * account_regressive
            account_regressive -= 1

    mult_tot_value_per_ten = tot_sum_multi_numbers * 10

    rest_division_per_eleven = mult_tot_value_per_ten % 11

    result_last_digit = 0 if rest_division_per_eleven > 9 else rest_division_per_eleven

    return result_last_digit


if __name__ == "__main__":

    flag = True

    while flag:

        try:

            CPF = str(input("Type a CPF here: "))  # '746.824.890-70'

            first_digit = valid_first_digit_cpf(CPF)

            second_list = valid_second_digit_cpf(CPF, first_digit)

            if str(first_digit) + str(second_list) == CPF[-2:]:
                print("CPF is valid!")
                break
            else:
                print("CPF not is valid! Try again.")
                continue

        except ValueError:
            print("Caracters invalid. Type only caracter valided.")
            continue
