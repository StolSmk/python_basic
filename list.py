def return_result_list(original_list):
    return [original_list[i] for i in range(1, len(original_list)) if original_list[i] > original_list[i - 1]]