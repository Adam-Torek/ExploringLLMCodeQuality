"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""


def text_lowercase_underscore(text):
    """
    :param text: str
    :return: bool
    """
    if text.islower() and '_' in text:
        return True
    else:
        return False


if __name__ == '__main__':
    print(text_lowercase_underscore("aab_cbbbc"))
    print(text_lowercase_underscore("aab_cbbbc_"))
    print(text_lowercase_underscore("aab_cbbbc_d"))
    print(text_lowercase_underscore("aab_cbbbc_d_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_k"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_k_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_k_l"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_k_l_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_k_l_m"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_k_l_m_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_k_l_m_n"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_k_l_m_n_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_k_l_m_n_o"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_k_l_m_n_o_"))
    print(text_lowercase_underscore("aab_cbbbc_d_e_f_g_h_i_j_k_l_m_n_o_p"))
    print(text_