from django.test import TestCase
from .models import Comment, Business,Profile,Post
# Create your tests here.
class CommentTestCase(TestCase):
    '''
    setup
    '''
    def setUp(self):
        self.comment = Comment(name='lovely')
    '''
    test instance of comment
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))
        '''
        test for save instance of comment
        '''
    def test_save_comment(self):
        self.comment.save_comment()
        name = Comment.objects.all()
        self.assertTrue(len(name)>0)


class profileTestCLass(TestCase):
    '''
    setup self instance of profile
    '''
    def setUp(self):
        self.prof = Profile(Bio='Live the moment')
    
    ''' 
    test instance of profile
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

    def test_save_profile(self):
        self.prof.save_profile()
        bio = Profile.objects.all()
        self.assertTrue(len(bio)>0)

class BusinessTestCase(TestCase):
    '''
    setup
    '''
    def setUp(self):
        self.business = Business(name='soko',image='soko.jpeg',pub_date='12,Oct,2018',user='1',NeighborHood='1')
    '''
    test instance of business
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
        '''
        test for save instance of business
        '''
    def test_save_business(self):
        self.business.save_business()
        name = Business.objects.all()
        self.assertTrue(len(name)>0)
