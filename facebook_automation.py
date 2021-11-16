#imprting important library for making our automation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#here we are blocking unwanted push notification from facebook

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chromeOptions.add_experimental_option("prefs", prefs)
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-setuid-sandbox")
chromeOptions.add_argument("--remote-debugging-port=9222")

chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-gpu")
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("disable-infobars")

driver = webdriver.Chrome(chrome_options=chromeOptions)

class facebook_feature:

    def __init__(self,username,password,caption,img_path):
        self.username = username
        self.password = password
        self.caption = caption
        self.img_path = img_path
        self.count = 0
    def Facebook_login(self):
        # Here we are loging into facebook
        driver.get("https://facebook.com")

        driver.maximize_window()

        email = driver.find_element_by_xpath('//*[@id="email"]')

        email_type = email.send_keys(self.username)

        password = driver.find_element_by_xpath('//*[@id="pass"]')

        password_type = password.send_keys(self.password)

        login = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

        login.click()

    def switch_page(self):
        # Here we are switching to page

        time.sleep(5)
        switch = driver.find_element_by_xpath("//div[@aria-label='Account']")

        time.sleep(3)

        switch.click()

        time.sleep(3)

        switch_profile = driver.find_element_by_xpath(
            "//body/div/div/div/div/div[@role='banner']/div/div/div/div/div/div/div/div/div[@aria-label='Account']/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/i[1]")

        time.sleep(2)

        switch_profile.click()

        time.sleep(2)

        switch_profile1 = driver.find_element_by_xpath(
            "//div[@role='radio']//div//div//div//div//div//div//span[@dir='auto'][normalize-space()='Beauty']")

        time.sleep(3)

        switch_profile1.click()

        time.sleep(6)

        # here we are finding group

        group = driver.find_element_by_xpath("//span[contains(text(),'Groups')]").click()

        time.sleep(5)

        self.group_auto_scroller()

    def photo_poster(self):
        print('trying')
        x = "'What's on your mind, Beauty?'"
        y = "//span[normalize-space()=""]"
        z = y[0:-1] + x + y[-1:]

        # print(z)

        # print('''//span[normalize-space()="What's on your mind, Beauty?"]''')

        time.sleep(7)
        print('finding')

        photo_poster = driver.find_element_by_xpath(
            "//body/div/div/div/div/div/div/div/div/div/div[@aria-label='Preview of a group']/div/div/div[@role='main']/div/div[@data-pagelet='DiscussionRootSuccess']/div/div/div/div/div[@data-pagelet='GroupInlineComposer']/div/div/div/div[1]/div[1]")
        photo_poster.click()
        time.sleep(5)

        print('clicking it')

        try:
            # time.sleep(2)
            # rules = driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/div/div/div/div/div[@role='dialog']/div/div/form[@method='POST']/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]")
            # rules.click()
            time.sleep(1.5)
            driver.find_element_by_xpath("//div[@aria-label='Got It']").click()

        except:
            pass

        time.sleep(5)
        try:
            photo_poster2 = driver.find_element_by_xpath("//div[@aria-label='Write something...']").send_keys(self.caption)
            time.sleep(2)
            temp_photo_poster = driver.find_element_by_xpath("//span[@data-text='true']")
            temp_photo_poster.send_keys(Keys.ENTER)

        except:
            photo_poster2_1 = driver.find_element_by_xpath("//div[@aria-label='Create a public post…']").send_keys(
                self.caption)
            time.sleep(2)
            temp_photo_poster1 = driver.find_element_by_xpath("//span[@data-text='true']")
            temp_photo_poster1.send_keys(Keys.ENTER)
            pass

        time.sleep(5)

        """photo_poster3 = driver.find_element_by_xpath(
            "//div[@class='dwxx2s2f dicw6rsg kady6ibp rs0gx3tq']//input[@type='file']").send_keys(self.img_path)

        time.sleep(5)
        
        # here we are posting photo"""
        photo_poster4 = driver.find_element_by_xpath(
            "//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 d1544ag0 tw6a2znq s1i5eluu tv7at329']")

        time.sleep(7)

        photo_poster4.click()

    def group_finder(self):
        z = 0
        str1 = '''//span[@dir='auto']//span//span[contains(text(),)]'''
        group_list = []
        group_list1 = []
        f = open("Group_list.txt", encoding="utf8")
        count_1 = f.readlines()
        for i in range(len(count_1)):
            str2 = count_1[i]
            group_list.append(str2[0:-1])
            # print(group_list)

            str3 = str1[0:-2] + group_list[i] + str1[-2:]
            group_list1.append(str3)

            # print(str3)

        for s in range(len(group_list1)):
            time.sleep(3)

            try:

                model_group = driver.find_element_by_xpath(group_list1[s+37]).click()

                print(s+37)
                #self.photo_poster()
                self.group_inviter()
                time.sleep(3)
            except:
                pass

    def auto_scrolling(self):
        max_time = 2
        start_time = time.time()  # remember when we started
        while (time.time() - start_time) < max_time:
            time.sleep(0.5)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    def group_auto_scroller(self):
        max_time = 20
        start_time = time.time()
        while(time.time()-start_time)<max_time:

            driver.find_element_by_xpath("//div[@aria-label='List of groups']//div[6]//a[1]").send_keys(Keys.END)
            time.sleep(0.25)


    def group_inviter(self):
        temp1 = driver.find_element_by_xpath(
            "//a[@aria-label='Profile']//div[@class='s45kfl79 emlxlaya bkmhp75w spb7xbtv oaz4zybt pmk7jnqg j9ispegn kr520xx4']")

        temp1.click()
        time.sleep(8)
        self.auto_scrolling()

        count_invited = 0
        like_list = []

        for i in range(1000):
            try:

                # time.sleep(20)
                time.sleep(0.01)
                temp2 = driver.find_element_by_xpath(f"//span[@class='pcp91wgn'][normalize-space()='{i}']")
                x = temp2.text
                like_list.append(x)
                like_list.remove('')
                like_list = [int(i) for i in like_list]
            except:
                pass
        print(like_list)

        for i in like_list:
            time.sleep(2)
            #print("group_like", i)
            #print(type(i))
            opener = driver.find_element_by_xpath(f"//span[@class='pcp91wgn'][normalize-space()='{i}']")
            print('found list')
            time.sleep(2)
            opener.click()
            time.sleep(2)
            for j in range(int(i)):
                #print(f'like start from {j} and end to{int(i)}')
                #print("trying")
                try:
                    driver.find_element_by_xpath("(//div[@aria-label='Invited'])").send_keys(Keys.END)
                    temp3 = driver.find_element_by_xpath("(//div[@aria-label='Invite'])")
                    rews = temp3.text
                    #print(rews)
                    if rews == "Invite":
                        time.sleep(1.2)
                        temp3.click()
                        self.count += 1
                        # print(count)
                    else:
                        pass
                except:
                    pass
            print(f'{self.count} has been completed')

            driver.find_element_by_xpath("//div[@aria-label='Close']").click()
            time.sleep(5)
        time.sleep(5)
        driver.find_element_by_xpath("//div[@aria-label='Back to previous page']").click()
        return self.count
