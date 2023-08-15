import OpenDartReader as od
import common

def ex_func():
    api_key = common.od_api_key

    print("OpenDart 객체를 초기화합니다...")
    dart = od(api_key)

    print("현대제철의 기업 고유코드를 검색합니다...")
    now_code = dart.find_corp_code('현대제철')
    print("현대제철의 코드는:", now_code)

    print("현대제철의 2023년 반기보고서를 불러옵니다...")

    hd = dart.finstate(now_code, 2023, 11012)
    hd_fs_con = hd[hd['fs_nm'] == '연결재무제표']
    hd_fs = hd[hd['fs_nm'] == '재무제표']

    print("연결재무제표와 재무제표의 자본총계를 각각 읽습니다...")

    # 연결재무제표 자본총계
    fs_con_total = hd_fs_con[hd_fs_con['account_nm'] == '자본총계']['thstrm_amount']
    fs_con_total = float(fs_con_total.values[0].replace(',', ''))
    print("연결재무제표 자본총계:", fs_con_total)
    if fs_con_total * 0.05 < 1e10:
        print(fs_con_total, "* 0.05 < 10,000,000,000이므로, 공시")
    else:
        print(fs_con_total, "* 0.05 >= 10,000,000,000이므로, 공시 X")

    # 재무제표 자본총계
    fs_total = hd_fs[hd_fs['account_nm'] == '자본총계']['thstrm_amount']
    fs_total = float(fs_total.values[0].replace(',', ''))
    print("재무제표 자본총계:", fs_total)
    if fs_total * 0.05 < 1e10:
        print(fs_total, "* 0.05 < 10,000,000,000이므로, 공시")
    else:
        print(fs_total, "* 0.05 >= 10,000,000,000이므로, 공시 X")


if __name__ == "__main__":
    ex_func()