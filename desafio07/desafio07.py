def passwordCracker(passwords, loginAttempt):
    memo = {}
    
    def backtrack(remaining_attempt):
        if remaining_attempt == "":
            return []
        if remaining_attempt in memo:
            return memo[remaining_attempt]
        
        for password in passwords:
            if remaining_attempt.startswith(password):
                result = backtrack(remaining_attempt[len(password):])
                if result is not None:
                    memo[remaining_attempt] = [password] + result
                    return memo[remaining_attempt]
        
        memo[remaining_attempt] = None
        return None
    
    result = backtrack(loginAttempt)
    
    if result is None:
        return "WRONG PASSWORD"
    else:
        return ' '.join(result)

# Testes
test_cases = [
    (["because", "can", "do", "must", "we", "what"], "wedowhatwemustbecausewecan", "we do what we must because we can"),
    (["hello", "planet"], "helloworld", "WRONG PASSWORD"),
    (["ab", "abcd", "cd"], "abcd", "ab cd"),  # Note that "abcd" is also a valid output
    (["ozkxyhkcst", "xvglh", "hpdnb", "zfzahm"], "zfzahm", "zfzahm"),
    (["gurwgrb", "maqz", "holpkhqx", "aowypvopu"], "gurwgrb", "gurwgrb"),
    (["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"], "aaaaaaaaaab", "WRONG PASSWORD"),
    (["ejevas", "drdv", "mgxucpnh", "wqixbctfd", "kmmam", "kjquwvis", "liznldbnh", "pivoicfu", "espropqatm", "dbrasoqg"], "cfuwqixbctfdliznldbnhkmmamlsprmpqatmljevaskmmamwqixbctfdpivoicauwgixbctfdmgxucpnhejevasdrdvpivoicfuliznldbnh", "WRONG PASSWORD"),
    (["okweif", "rpgnteja", "ufemijimuw", "vpon", "eoncaf", "udgf", "hhtez", "aiknzgy", "bpndljur", "eeycbwv"], "ufemijimuweeycbwvokweifvponbpndljurudgfaiknzgyhhtezufemijimuwufemijimuwaiknzgyudgfufemijimuwrpgntejaeoncafvponudgfbpndljurokweifhhtezbpndljurvponufemijimuwudgfbpndljurufemijimuweoncafrpgntejaudgf", "ufemijimuw eeycbwv okweif vpon bpndljur udgf aiknzgy hhtez ufemijimuw ufemijimuw aiknzgy udgf ufemijimuw rpgnteja eoncaf vpon udgf bpndljur okweif hhtez bpndljur vpon ufemijimuw udgf bpndljur ufemijimuw eoncaf rpgnteja udgf"),
]

for i, (passwords, loginAttempt, expected) in enumerate(test_cases):
    result = passwordCracker(passwords, loginAttempt)
    assert result == expected, f"Teste {i + 1} falhou: esperado {expected}, mas obteve {result}"
    print(f"Teste {i + 1} passou: obteve {result}")
