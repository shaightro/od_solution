# This Python file uses the following encoding: euc-kr
import OpenDartReader as od
import common

if __name__ == "__main__":
    api_key = common.od_api_key

    print("OpenDart ��ü�� �ʱ�ȭ�մϴ�...")
    dart = od(api_key)

    print("������ö�� ��� �����ڵ带 �˻��մϴ�...")
    now_code = dart.find_corp_code('������ö')
    print("������ö�� �ڵ��:", now_code)

    print("������ö�� 2023�� �ݱ⺸���� �ҷ��ɴϴ�...")

    hd = dart.finstate(now_code, 2023, 11012)
    hd_fs_con = hd[hd['fs_nm'] == '�����繫��ǥ']
    hd_fs = hd[hd['fs_nm'] == '�繫��ǥ']

    print("�����繫��ǥ�� �繫��ǥ�� �ں��Ѱ踦 ���� �н��ϴ�...")

    # �����繫��ǥ �ں��Ѱ�
    fs_con_total = hd_fs_con[hd_fs_con['account_nm'] == '�ں��Ѱ�']['thstrm_amount']
    fs_con_total = float(fs_con_total.values[0].replace(',', ''))
    print("�����繫��ǥ �ں��Ѱ�:", fs_con_total)
    if fs_con_total * 0.05 < 1e10:
        print(fs_con_total, "* 0.05 < 10,000,000,000�̹Ƿ�, ����")
    else:
        print(fs_con_total, "* 0.05 >= 10,000,000,000�̹Ƿ�, ���� X")

    # �繫��ǥ �ں��Ѱ�
    fs_total = hd_fs[hd_fs['account_nm'] == '�ں��Ѱ�']['thstrm_amount']
    fs_total = float(fs_total.values[0].replace(',', ''))
    print("�繫��ǥ �ں��Ѱ�:", fs_total)
    if fs_total * 0.05 < 1e10:
        print(fs_total, "* 0.05 < 10,000,000,000�̹Ƿ�, ����")
    else:
        print(fs_total, "* 0.05 >= 10,000,000,000�̹Ƿ�, ���� X")

