class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(i for i in s if i.isalnum())
        check = st.lower()
        if check == check[::-1]: return True
        else: return False

        