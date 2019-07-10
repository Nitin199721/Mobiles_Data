from lxml import html
import requests
from .forms import InputForm
from django.shortcuts import render
from .models import MobileData



def scraper(url):

    res = requests.get(url)
    tree = html.fromstring(res.content)

    txt = tree.xpath('//*[@class="btn btn-blue-filled btn-load-more"]/text()')
    i = 1
    urls = []
    while i <= 1:
        url = 'https://www.phonecurry.com/best-phones?page=' + str(i)
        print(i)
        i += 1
        res = requests.get(url)
        tree = html.fromstring(res.content)
       # txt = tree.xpath('//*[@class="btn btn-blue-filled btn-load-more"]/text()')
        urls.extend(tree.xpath('//*[@class="phone-name"]/@href'))
    mobile_list = []

    for i, url1 in enumerate(urls):

        mobile_row = []
        resp1 = requests.get(url1)
        tree1 = html.fromstring(resp1.content)
        mobile_row.append(tree1.xpath('//*[@class="phone-name"]/span/text()')[0] if len(tree1.xpath('//*[@class="phone-name"]/span/text()')) > 0 else "NA")
        p = tree1.xpath('//p[1][@class="phone-sub-details"]/span[2]/text()')
        mobile_row.extend(p if len(p) > 0 else "NA")
        mobile_row.append(tree1.xpath('//*[@id="specs"]/section/div/table[1]/tbody/tr/td[2]/text()')[0] if len(tree1.xpath('//*[@id="specs"]/section/div/table[1]/tbody/tr/td[2]/text()')) > 0 else "NA")
        mobile_row.append(tree1.xpath('//*[@id="productImg"]/img[1]/@src')[0] if len(tree1.xpath('//*[@id="productImg"]/img[1]/@src')) > 0 else "NA")
        mobile_row.append(tree1.xpath('//*[@id="specs"]/section/div/table[2]/tbody//td[text()="Screen Resolution"]//following-sibling::td/text()')[0] if len(tree1.xpath('//*[@id="specs"]/section/div/table[2]/tbody//td[text()="Screen Resolution"]//following-sibling::td/text()')) > 0 else "NA")

        mobile_row.append(tree1.xpath('//*[@id="specs"]/section/div/table[2]/tbody//td[text()="Screen Size"]//following-sibling::td/text()')[0] if len(tree1.xpath('//*[@id="specs"]/section/div/table[2]/tbody//td[text()="Screen Size"]//following-sibling::td/text()')) > 0 else"NA")

        mobile_row.append(tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody//td[text()="Processor"]//following-sibling::td/text()')[0] if len(tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody//td[text()="Processor"]//following-sibling::td/text()')) > 0 else "NA")

        mobile_row.append(tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody//td[text()="GPU"]//following-sibling::td/text()')[0] if len(tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody//td[text()="GPU"]//following-sibling::td/text()')) > 0 else "NA")

        mobile_row.append(tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody//td[text()="RAM"]//following-sibling::td/text()')[0] if len(tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody//td[text()="RAM"]//following-sibling::td/text()')) > 0 else "NA")

        mobile_list.append(mobile_row)

    return mobile_list
# our view which is a function named index

# get forms file and render content
def list_phone(request, name):
    print(name)
    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            data = scraper(form.cleaned_data['Url_field'])
            print(data)

            # MobileData.objects.bulk_create([MobileData(*item) for item in data])
            for i in data:
                obj = MobileData()
                obj.Name = i[0]
                obj.Price = i[1]
                obj.SmartPhone_OS = i[2]
                obj.Img_Path = i[3]
                obj.ScreenResolution = i[4]
                obj.ScreenSize = i[5]
                obj.Processor = i[6]
                obj.GPU = i[7]
                obj.RAM = i[8]
                obj.save()
            data1 = MobileData.objects.all()
            context = {"q": data1, "username": name, "email": email}
            return render(request, "MobileData.html", context)


def get_url(request):
        form = InputForm()
        return render(request, 'index.html', {'form': form})


