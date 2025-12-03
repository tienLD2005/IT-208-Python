import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

DATA_FILE = "data.csv"


def tinh_xep_loai(diem_tb):
    """Xác định xếp loại dựa vào điểm trung bình.

    Args:
        diem_tb (float): Điểm trung bình.

    Returns:
        str: Xếp loại tương ứng.
    """
    if diem_tb >= 8:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5:
        return "Trung Bình"
    else:
        return "Yếu"


def load_data():
    """Load dữ liệu sinh viên từ file CSV.

    Returns:
        list: Danh sách sinh viên dạng list[dict].
    """
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE).to_dict(orient="records")
    return []


def save_data(data):
    """Lưu danh sách sinh viên vào file CSV.

    Args:
        data (list): Danh sách sinh viên.
    """
    df = pd.DataFrame(data)
    df.to_csv(DATA_FILE, index=False)
    print("✔ Đã lưu dữ liệu vào file data.csv")


def hien_thi(data):
    """Hiển thị danh sách sinh viên dưới dạng bảng.

    Args:
        data (list): Danh sách sinh viên.
    """
    if not data:
        print("⚠ Không có sinh viên nào.")
        return

    df = pd.DataFrame(data)
    print(df.to_string(index=False))


def them_sinh_vien(data):
    """Thêm sinh viên mới vào danh sách.

    Args:
        data (list): Danh sách sinh viên.
    """
    ma = input("Nhập mã sinh viên: ")

    if any(sv["id"] == ma for sv in data):
        print("❌ Mã sinh viên đã tồn tại!")
        return

    ten = input("Nhập tên sinh viên: ")

    try:
        toan = float(input("Điểm Toán: "))
        ly = float(input("Điểm Lý: "))
        hoa = float(input("Điểm Hóa: "))

        if not all(0 <= x <= 10 for x in [toan, ly, hoa]):
            print("❌ Điểm phải trong khoảng 0-10!")
            return

        diem_tb = round((toan + ly + hoa) / 3, 2)
        xep_loai = tinh_xep_loai(diem_tb)

        data.append({
            "id": ma,
            "ten": ten,
            "diem_toan": toan,
            "diem_ly": ly,
            "diem_hoa": hoa,
            "diem_tb": diem_tb,
            "xep_loai": xep_loai
        })

        print("✔ Thêm sinh viên thành công!")
    except ValueError:
        print("❌ Điểm phải là số!")


def cap_nhat(data):
    """Cập nhật điểm số của sinh viên theo mã.

    Args:
        data (list): Danh sách sinh viên.
    """
    ma = input("Nhập mã sinh viên cần cập nhật: ")

    for sv in data:
        if sv["id"] == ma:
            try:
                sv["diem_toan"] = float(input("Điểm Toán mới: "))
                sv["diem_ly"] = float(input("Điểm Lý mới: "))
                sv["diem_hoa"] = float(input("Điểm Hóa mới: "))

                sv["diem_tb"] = round(
                    (sv["diem_toan"] + sv["diem_ly"] + sv["diem_hoa"]) / 3, 2
                )
                sv["xep_loai"] = tinh_xep_loai(sv["diem_tb"])

                print("✔ Cập nhật thành công!")
            except ValueError:
                print("❌ Điểm phải là số!")
            return

    print("❌ Không tìm thấy sinh viên!")


def xoa(data):
    """Xóa sinh viên khỏi danh sách theo mã.

    Args:
        data (list): Danh sách sinh viên.
    """
    ma = input("Nhập mã sinh viên cần xóa: ")

    for sv in data:
        if sv["id"] == ma:
            xac_nhan = input("Bạn có chắc muốn xóa? (y/n): ")
            if xac_nhan.lower() == "y":
                data.remove(sv)
                print("✔ Đã xóa sinh viên.")
            return

    print("❌ Không tìm thấy sinh viên!")


def tim_kiem(data):
    """Tìm kiếm sinh viên theo mã hoặc tên gần đúng.

    Args:
        data (list): Danh sách sinh viên.
    """
    tu_khoa = input("Nhập mã hoặc tên sinh viên: ").lower()

    ket_qua = [
        sv for sv in data
        if tu_khoa in sv["id"].lower() or tu_khoa in sv["ten"].lower()
    ]

    if ket_qua:
        hien_thi(ket_qua)
    else:
        print("❌ Không tìm thấy sinh viên!")


def sap_xep(data):
    """Sắp xếp danh sách sinh viên theo điểm TB hoặc tên.

    Args:
        data (list): Danh sách sinh viên.
    """
    print("1. Sắp xếp theo điểm TB giảm dần")
    print("2. Sắp xếp theo tên A-Z")
    chon = input("Chọn kiểu sắp xếp: ")

    if chon == "1":
        data.sort(key=lambda sv: sv["diem_tb"], reverse=True)
        print("✔ Đã sắp xếp theo điểm TB.")
    elif chon == "2":
        data.sort(key=lambda sv: sv["ten"])
        print("✔ Đã sắp xếp theo tên.")
    else:
        print("❌ Lựa chọn không hợp lệ!")


def thong_ke(data):
    """Thống kê số lượng sinh viên theo từng xếp loại.

    Args:
        data (list): Danh sách sinh viên.

    Returns:
        Series: Thống kê dạng pandas.Series.
    """
    df = pd.DataFrame(data)
    counts = df["xep_loai"].value_counts()

    print("\n📊 THỐNG KÊ XẾP LOẠI:")
    print(counts)

    return counts


def ve_bieu_do(data):
    """Vẽ biểu đồ cột hoặc tròn dựa trên thống kê xếp loại.

    Args:
        data (list): Danh sách sinh viên.
    """
    counts = thong_ke(data)

    print("\n1. Biểu đồ cột")
    print("2. Biểu đồ tròn")
    chon = input("Chọn kiểu biểu đồ: ")

    plt.figure()

    if chon == "1":
        counts.plot(kind="bar")
        plt.title("Thống kê xếp loại")
        plt.xlabel("Xếp loại")
        plt.ylabel("Số lượng")

    elif chon == "2":
        counts.plot(kind="pie", autopct="%1.1f%%")
        plt.title("Tỷ lệ xếp loại")

    else:
        print("❌ Lựa chọn không hợp lệ!")
        return

    plt.tight_layout()

    # ⭐ Quan trọng: KHÔNG chặn chương trình
    plt.show(block=False)

    print("✔ Biểu đồ đã mở. Quay lại menu...")



def menu():
    """Menu điều khiển CLI của chương trình."""
    data = load_data()

    while True:
        print("\n====== MENU QUẢN LÝ SINH VIÊN ======")
        print("1. Hiển thị danh sách")
        print("2. Thêm sinh viên")
        print("3. Cập nhật sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm")
        print("6. Sắp xếp")
        print("7. Thống kê điểm TB")
        print("8. Vẽ biểu đồ")
        print("9. Lưu dữ liệu")
        print("10. Thoát")

        chon = input("Chọn chức năng: ")

        if chon == "1":
            hien_thi(data)
        elif chon == "2":
            them_sinh_vien(data)
        elif chon == "3":
            cap_nhat(data)
        elif chon == "4":
            xoa(data)
        elif chon == "5":
            tim_kiem(data)
        elif chon == "6":
            sap_xep(data)
        elif chon == "7":
            thong_ke(data)
        elif chon == "8":
            ve_bieu_do(data)
        elif chon == "9":
            save_data(data)
        elif chon == "10":
            save_data(data)
            print("👋 Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    menu()
