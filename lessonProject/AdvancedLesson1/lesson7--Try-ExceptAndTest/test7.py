import unittest
from surveyClass import Survey
class TestSurvey(unittest.TestCase):
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        #使用问题创建一个实例，并调用类中的方法
        my_survey = Survey(question)
        my_survey.store_response('English')
        #使用断言来判断“English”这个答案被妥善存储了
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = Survey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)
unittest.main()
