import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import average_true_range


class TestAverageTrueRange(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.close_data = SampleData().get_sample_close_data()

        self.atr_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, 9.7000000000000259,
        9.4250000000000131, 9.1958333333333364, 9.3281944444444491,
        9.4384953703703758, 11.652079475308652, 14.113399562757204,
        18.287832968964349, 20.784860807470306, 24.819050672891922,
        25.822542227409922, 26.042118522841601, 25.886765435701335,
        25.757304529751114, 25.649420441459267, 25.559517034549391,
        23.559597528791169, 21.372997940659317, 19.447498283882755,
        17.90458190323562, 16.618818252696339, 15.682348543913617,
        18.558623786594669, 20.955519822162213, 22.952933185135169,
        27.855777654279308, 33.006481378566086, 37.298734482138407,
        37.787278735115343, 36.771065612596125, 35.7892213438301,
        34.971017786525081, 33.942514822104222, 34.695429018420171,
        35.141190848683458, 34.897659040569557, 32.926382533807953,
        31.745318778173299, 29.519432315144414, 27.664526929287007,
        25.405439107739173, 23.546199256449313, 24.438499380374424,
        24.113749483645353, 23.929791236371127, 23.776492696975936,
        22.715410580813273, 20.611175484011046, 19.419312903342526,
        18.426094086118759, 17.598411738432286, 16.908676448693559,
        16.388897040577959, 14.270747533814957, 12.50562294484579,
        12.034685787371481, 11.753904822809572, 11.519920685674649,
        11.653267238062215, 11.929389365051856, 12.157824470876557,
        12.826520392397143, 14.115433660330963, 15.189528050275811,
        16.084606708563186, 15.832172257135978, 15.278476880946647,
        14.817064067455538, 14.472553389546283, 14.453794491288571,
        15.296495409407141, 16.003746174505945, 16.593121812088281,
        17.084268176740228, 17.26522348061685, 17.416019567180701,
        17.541682972650577, 15.788069143875477, 14.151724286562903,
        12.788103572135759, 11.538419643446479, 10.557016369538749,
        10.189180307948961, 10.399316923290808, 10.636097436075664,
        10.335081196729709, 10.11423433060809, 9.6618619421734042,
        9.219884951811169, 8.8999041265093002, 8.6332534387577429,
        7.7377111989647842, 6.9914259991373191, 7.699521665947767,
        8.2896013882898085, 8.6130011569081777, 8.7908342974234728,
        9.9240285811862137, 14.120023817655181, 18.261686514712654,
        22.433072095593889, 25.930893412994919, 27.245744510829109,
        24.609787092357603, 21.76815591029801, 19.118463258581674,
        16.945386048818047, 18.06282170734837, 18.627351422790316,
        20.122792852325265, 20.757327376937713, 21.631106147448094,
        21.029255122873408, 22.281045935727832, 22.775871613106528,
        23.58322634425544, 23.371021953546208]

        self.atr_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        11.478750000000019, 12.88390625000002, 14.575917968750012,
        17.967678222656264, 20.935468444824238, 24.678534889221208,
        27.233718028068559, 29.46950327455999, 29.64081536523998,
        29.328213444584982, 28.800936764011862, 28.339569668510382,
        27.935873459946585, 27.582639277453264, 25.829809367771613,
        24.284833196800165, 22.522979047200138, 21.082606666300123,
        22.564780833012598, 23.861683228886015, 24.996472825275255,
        28.41816372211585, 32.210893256851364, 35.529531599744942,
        38.433340149776825, 40.974172631054721, 40.881151052172882,
        39.73225717065128, 38.62572502431987, 38.605009396279875,
        38.586883221744884, 38.888522819026775, 39.822457466648416,
        40.75965028331737, 39.447193997902701, 37.746294748164871,
        35.326757904644261, 33.209663166563729, 32.670955270743264,
        32.479585861900354, 32.377137629162803, 31.206245425517452,
        30.181714747327767, 29.285250403911796, 28.222094103422819,
        26.376832340494957, 24.762228297933078, 23.349449760691435,
        22.154518540605, 21.108953723029369, 20.194084507650693,
        18.879823944194349, 17.813595951170058, 16.880646457273805,
        16.593065650114585, 16.465182443850267, 16.070784638368991,
        16.083186558572876, 16.642788238751272, 17.13243970890737,
        17.560884745293954, 18.552024152132212, 19.636771133115687,
        19.220924741476217, 18.412059148791691, 17.905551755192732,
        18.10610778579364, 18.285344312569428, 18.442176273498244,
        18.579404239310961, 18.699478709397084, 18.804543870722444,
        18.725225886882132, 18.655822651021861, 18.595094819644125,
        17.148207967188608, 15.847181971290032, 14.753784224878782,
        13.953311196768936, 13.640397297172825, 13.700347635026223,
        13.752804180647946, 13.578703658066955, 13.188865700808575,
        12.946507488207503, 12.43319405218157, 11.791544795658869,
        11.230101696201505, 10.738838984176311, 10.801484111154274,
        10.85629859725999, 10.904261272602492, 10.946228613527181,
        11.595450036836281, 15.282268782231736, 18.991985184452759,
        22.029237036396175, 24.703082406846661, 27.04269710599084,
        29.478609967741995, 30.410033721774255, 28.162529506552481,
        25.738463318233418, 25.477405403454238, 25.248979728022455,
        25.817857262019643, 26.040625104267193, 26.520546966233795,
        27.659228595454572, 29.944325021022756, 29.768784393394906,
        29.91143634422054, 29.625006801192974]

        self.atr_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, 21.157000000000007, 24.384300000000003,
        27.301869999999997, 29.672682999999996, 31.217414699999996,
        32.607673229999996, 32.430905906999989, 31.901815316299992,
        31.222633784669995, 30.611370406202997, 30.061233365582702,
        29.566110029024436, 27.965499026122, 26.596949123509809,
        27.23125421115882, 27.802128790042936, 28.315915911038633,
        30.721324319934773, 33.52519188794129, 36.048672699147161,
        38.319805429232446, 40.363824886309203, 42.20344239767828,
        43.859098157910452, 43.49618834211941, 43.073569507907465,
        42.612212557116706, 42.45099130140504, 42.950892171264528,
        44.119802954138073, 45.062822658724265, 45.288540392851843,
        43.785686353566653, 41.991117718209992, 40.68200594638899,
        39.727805351750092, 38.921024816575077, 38.194922334917564,
        37.541430101425803, 36.08828709128322, 35.117458382154901,
        34.243712543939409, 32.897341289545466, 30.953607160590913,
        29.23724644453182, 27.692521800078634, 26.302269620070764,
        25.051042658063686, 23.924938392257314, 22.567444553031585,
        21.768700097728431, 21.148830087955595, 20.590947079160038,
        20.14885237124404, 20.189967134119641, 20.22697042070768,
        20.260273378636917, 20.783246040773228, 21.427921436695907,
        22.008129293026318, 22.554316363723689, 21.953884727351316,
        21.709496254616184, 21.49254662915456, 21.297291966239101,
        21.121562769615188, 20.963406492653668, 20.821065843388297,
        20.692959259049463, 20.577663333144514, 20.33689699983006,
        20.120207299847049, 19.92518656986234, 18.64266791287611,
        17.758401121588495, 17.272561009429644, 16.95730490848668,
        16.673574417638015, 16.472216975874222, 16.399995278286802,
        16.219995750458125, 15.787996175412308, 15.363196557871074,
        14.710876902083971, 13.96978921187557, 13.696810290688012,
        13.451129261619212, 13.230016335457293, 13.031014701911564,
        13.442913231720405, 16.36362190854836, 19.278259717693523,
        22.278433745924168, 24.991590371331746, 26.834431334198577,
        28.803988200778726, 30.576589380700863, 32.27193044263079,
        32.858737398367708, 32.593863658530935, 31.968477292677846,
        31.751629563410056, 31.556466607069048, 31.608819946362139,
        32.377937951725933, 34.122144156553347, 35.324929740898014,
        36.623436766808219, 36.052093090127393]

    def test_average_true_range_period_6(self):
        period = 6
        atr = average_true_range.average_true_range(self.close_data, period)
        np.testing.assert_array_equal(atr, self.atr_period_6_expected)

    def test_average_true_range_period_8(self):
        period = 8
        atr = average_true_range.average_true_range(self.close_data, period)
        np.testing.assert_array_equal(atr, self.atr_period_8_expected)

    def test_average_true_range_period_10(self):
        period = 10
        atr = average_true_range.average_true_range(self.close_data, period)
        np.testing.assert_array_equal(atr, self.atr_period_10_expected)

    def test_average_true_range_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            average_true_range.average_true_range(self.close_data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
