def question_prompt(coding, exp : None , company : None):
    if coding and exp and company:
        prompt_1 =f'''
    I am currently preparing to transition to a new job as a software engineer 
    and I am specifically interested in joining {company}. I have accumulated
    {exp} years of experience working with {coding} and related technologies.
    To assist me in this process, I would greatly appreciate if you ask me 
    interview question that may be asked in my interview.
    '''
        return prompt_1
    elif coding:
        prompt_2 = f'''
        I am currently preparing to transition to a new job as a software engineer.I am intested in {coding} and related technologies.To assist me in this process, I would greatly appreciate if you ask me interview question that may be asked in my interview.
        '''
        return prompt_2
    elif coding and exp:
        prompt_3 = f''' 
        I am currently preparing to transition to a new job as a software engineer.I have accumulated {exp} years of experience working with{coding} and related technologies.To assist me in this process, I would greatly appreciate if you ask me interview question that may be asked in my interview.
        '''
        return prompt_3
    elif coding and company:
        prompt_4 = f'''
        I am currently preparing to transition to a new job as a software engineer and I am specifically interested in joining {company}.I am intested in {coding} and related technologies.To assist me in this process, I would greatly appreciate if you ask me interview question that may be asked in my interview.
        '''
        return prompt_4
    
    def ans_prompt(question,ans):
        prompt_result = f'''I am providing an ans of question. please read the question carefully and then analyse the ans accordingly. and give your respose by keeping following thing in your mind:-
        1. how much % of ans is correct for the question?
        2. how much % of grammatical mistakes in ans?
        3. how much % of jumble words used in interview ?
        
        Please provide your answer with all above points and your suggestion too if any.
        '''