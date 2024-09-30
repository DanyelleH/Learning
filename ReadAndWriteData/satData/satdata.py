import json

class SatData:
    def __init__(self):
        with open("/Users/danyelleridley/Documents/Learning/ReadAndWriteData/satData/sat.json",'r') as infile:
            stat_data = json.load(infile)
            formatted_sat_data ={}# key: DBN, Value: List of DBN Data
            for dbn_list in stat_data["data"]:
                # school_name = dbn_list[9]
                # number_of_testers = dbn_list[10]
                # critical_reading_avg = dbn_list[11]
                # mathematics_mean = dbn_list[12]
                # writing_mean = dbn_list[13]
                # formatted_sat_data[dbn_list[8]] = f"{dbn_list[8]},{school_name},{number_of_testers},{critical_reading_avg},{mathematics_mean},{writing_mean}"
                # print(formatted_sat_data[dbn_list[8]])
                formatted_sat_data[dbn_list[8]] = ",".join([dbn_list[8], dbn_list[9], ("" if dbn_list[10] == None else dbn_list[10]),("" if dbn_list[11] == None else dbn_list[11]),("" if dbn_list[12] == None else dbn_list[12]),("" if dbn_list[13] == None else dbn_list[13])])# the key is whats in index 8 of the list.
            self._stat_data = formatted_sat_data

    def save_as_csv (self, DBN_list):
        with open("/Users/danyelleridley/Documents/Learning/ReadAndWriteData/satData/dbn.csv", "w") as outfile:
            outfile.write("DBM,School Name,Number of Test Takers,Critical Reading Mean,Mathematics Mean,Writing Mean" + "\n")# write headers to the file#
            for dbn in sorted(DBN_list):
                if dbn in self._stat_data:
                    outfile.write(self._stat_data[dbn]+ "\n")
        return

sd = SatData()
dbn_list = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbn_list)