

class Project:
    def __init__(self, big_title, year, category,description,award,img_url,source_url,demonstration_url,name):
        self.big_title = big_title
        self.name = name
        self.year = year
        self.category = category
        self.description = description
        self.img_url = img_url
        self.award = award
        self.source_url = source_url
        self.demonstration_url = demonstration_url




project_1 = Project(
    big_title = "To-Do List App",
    name = "GetDoneTask",
    year = "2018",
    category = "To Do List",
    description = "As part of exploring more about coding, I work on my first personal project which is an Iphone App using Swift and Xcode. The app implements many features including Core Data Database and CocoaPods. The most interesting feature would be swiping tasks like swiping Tinder dates. The app helps me win Congressional App Challenge Texas District 2",
    img_url = "static/images/congress_2.JPG",
    award = "Congressional Winner",
    source_url = "https://bitbucket.org/brian1223/getdonetask/src/master/",
    demonstration_url = "https://vimeo.com/manage/videos/377679963"
)

project_2 = Project(
    big_title = "Blog",
    name = "Thang's Blog",
    year = "2021",
    category = "Website",
    description = "The blog is built as a project from Python Course on Udemy by Angela Yu. It is built by HTML, CSS, and Python with Flask handling the back-end and user registration. It also uses Sqlalchemy to store the database of the users. The blog is where I share my voice. This is where I talk to the world.",
    img_url = "static/images/blog.jpg",
    award = "My Diary",
    source_url = "https://github.com/BrianTruong23/thang-blog",
    demonstration_url = "https://thang-blog.herokuapp.com/"
)

project_3 = Project(
    big_title = "VieTalk Website",
    name = "VieTalk Website",
    year = "2021",
    category = "Website",
    description = "VieTalk is a project that aims to teaches Vietnamese in an engaging and homey fashion with interactive activities. Students not only learn the language but also the culture and they can be a part of a Vietnamese community.This is the website that I personally design for the project.",
    img_url = "static/images/vieTalk.png",
    award = "Educational Website",
    source_url = "https://github.com/BrianTruong23/website_vieTalk_project",
    demonstration_url = "https://vietalk-project.herokuapp.com/?fbclid=IwAR3RdCYlORBc38J9egN8DMaR073Lt15kkQaEMMa8Abbpwcuj23-L2jfwN9E"
)





projects_list = [project_1,project_2, project_3]


