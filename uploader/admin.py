from django.contrib import admin
from uploader.models import *

# Register your models here.
admin.site.register(Syllabus, SyllabusAdmin)
admin.site.register(ExamBoard, ExamBoardAdmin)
admin.site.register(ExamLevel, ExamLevelAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(UnitTopic, UnitTopicAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Licence, LicenceAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Vote)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(Message, MessageAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(MultipleChoiceAnswer)
admin.site.register(MultipleChoiceUserAnswer, MultipleChoiceUserAnswerAdmin)
admin.site.register(Lesson)
admin.site.register(LessonItem, LessonItemAdmin)
admin.site.register(SyllabusFavourite)
admin.site.register(UnitFavourite)
admin.site.register(UnitTopicFavourite)
admin.site.register(Group)
admin.site.register(StudentGroup)
admin.site.register(UnitTopicLink)
admin.site.register(TestResult)
admin.site.register(Test)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)
admin.site.register(AssignmentSubmissionFile)
admin.site.register(Grading)
admin.site.register(GradeOptions)
admin.site.register(NumericalGrade)
admin.site.register(LessonPrePost)
admin.site.register(LessonPrePostResponse, LessonPrePostResponseAdmin)
admin.site.register(GroupLesson)
admin.site.register(Image, ImageAdmin)
admin.site.register(NoteHistory, NoteHistoryAdmin)
