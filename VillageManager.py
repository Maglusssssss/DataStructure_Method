from Village import Village

def read_village_from_file(fileName):
    """
    Hàm đọc tệp dữ liệu về phường. Hàm này thực hiện đọc dữ liệu từ các phường
    từ tệp fileName sau đó tạo ra các đối tượng Village tương ứng và lưu vào 1 danh 
    sách, sau khi kết thúc việc đọc dữ liệu, hàm này trả lại danh sách các phường
    đã tạo được.
    
    dữ liệu trong tệp fileName được lưu dưới dạng csv,
    dòng đầu tiên là tên các thuộc tính của phường: vid,name,town
    các dòng tiếp theo, mỗi dòng chứa thông tin của 1 phường, mỗi thông tin cách nhau bởi 1 dấu phẩy ,
    Ví dụ:
    vid,name,town
    D-00001,Phúc Xá,Ba Đình
    B-00004,Trúc Bạch,Ba Đình
    D-00006,Vĩnh Phúc,Ba Đình
    """
    res = []
    with open(fileName, 'rt') as f:
        data = f.readlines()
        for row in data[1:]:
            row = row.strip().split(",")
            res.append(Village(row[1], row[0], row[2]))
            
    return res
    
def read_village_student_from_file(fileName, village_list):
    
    """
    Hàm thực hiện việc đọc file số lượng thí sinh thi vào cấp 3 của mỗi phường để bổ sung thêm thông tin
    vào thuộc tính student của mỗi Village trong village_list,
    Nhiệm vụ của hàm này là đọc dữ liệu số lượng thí sinh thi vào cấp 3 theo năm và ghi vào thuộc tính student
    của phường đó. Chú ý là việc thêm thông tin cần theo đúng mã phường (vid) của phường đó.
    
    fileName chứa thông tin về số lượng thí sinh thi vào cấp 3 theo từng năm
    được lưu dưới dạng csv.
    Dòng đầu tiên là tên các thuộ
    
    Ví dụ về file:
    
    vid,2018,2019,2020,2021,2022,2023
    D-00001,7408,7554,7674,7775,7875,7969
    B-00004,6758,6883,6986,7074,7148,7277
    D-00006,7000,7114,7197,7331,7470,7566
    D-00007,7377,7492,7592,7710,7843,7942
    """
    with open(fileName, "rt") as f:
        data = f.readlines()
        header = data[0].strip().split(",")
        for row in data[1:]:
            row = row.strip().split(",")
            di = {header[i]:int(row[i]) for i in range(1, len(row))}
            for vill in village_list:
                if vill.vid == row[0]:
                    vill.student = di
                    
    
def get_Hanoi_student_change(village_list):
    """
    Hàm thực hiện trả về danh sách các năm (int)được sắp xếp tăng dần theo 
    số lượng thí sinh thi vào cấp 3 TĂNG THÊM mỗi năm trên toàn thành phố Hà Nội.
    output: [2019, 2020, 2021, 2022, 2023]
    """
    dic = {}
    for vill in village_list:
        for key in vill.student:
            if key in dic:
                dic[key] += vill.student[key]
            else:
                dic[key] = vill.student[key]
    di_sort = sorted(dic)
    return di_sort.keys
    
def get_top_village_by_year(village_list, rank, year):
    
    """
    Hàm trả về 1 danh sách tên phường với xếp hạng ( = rank) 
    và có số lượng thí sinh trong năm (year) 
    lớn hơn giá trị trung bình của tất cả số thí sinh của thành phố Hà Nội trong năm đó
    Danh sách được sắp sếp theo số lượng thí sinh.
    
    Ví dụ: rank = 2, year = 2018
    Tìm tất cả tên phường trong đó phường là phường loại 2 có số thí sinh thi vào cấp 3 
    năm 2018 lớn hơn trung bình số thí sinh thi vào cấp 3 năm 2018 trên toàn thành phố Hà Nội.
    output: ['Cống Vị',...,'Yên Hòa']
    """
    dic = {}
    for vill in village_list:
        for key in vill.student:
            if key in dic:
                dic[key] += vill.student[key]
            else:
                dic[key] = vill.student[key]
                
    res = []
    for vill in village_list:
        if vill.get_rank() == rank and vill.student[year] > dic['year'] / len(village_list):
            res.append([vill.name, vill.student[year]])
    list_sort = sorted(res, key=lambda x: x[1])
    return [ row[0] for row in list_sort]
    
def sorted_town_by_avg_student(village_list):
    
    """
    Hàm trả về một danh sách các quận (town) được xắp sếp tăng dần
    theo số lượng thí sinh thi cấp 3 trung bình của các phường trong quận đó.
    Giá trị trung bình được tính trên tất cả các năm cho tất cả các phường thuộc quận đó
    
    output: ['Ba Đình','Cầu Giấy','Hoàn Kiếm','Long Biên','Tây Hồ']
    """
    res = []
    for vill in village_list:
        avg_student = sum(vill.student.values())/len(vill.student.values())
        res.append([vill.name, avg_student])
    list_sort = sorted(res, key=lambda x: x[1])
    return [ row[0] for row in list_sort]
    