"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""

def text_lowercase_underscore(string):
    if string.islower() and "_" in string:
        return True
    else:
        return False

print(text_lowercase_underscore("aab_cbbbc")) # True
print(text_lowercase_underscore("Aab_Cbbbc")) # False
print(text_lowercase_underscore("aabb_cbbbc")) # False
print(text_lowercase_underscore("aab_Cbbbc")) # False
print(text_lowercase_underscore("aabb_cbbbc_")) # True
print(text_lowercase_underscore("aabb_Cbbbc_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_j")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_j_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_j_k")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_j_k_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_j_k_l")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_j_k_l_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_j_k_l_m")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_j_k_l_m_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_j_k_l_m_n")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_j_k_l_m_n_")) # False
print(text_lowercase_underscore("aabb_cbbbc_d_e_f_g_h_i_