import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import standard_variance


class TestStandardVariance(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.sv_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        43.004616666666188, 12.411866666666613, 13.249626666666739,
        6.8342566666668771, 6.8819866666668315, 6.4659366666667042,
        8.4007599999999023, 7.9339466666666043, 14.489346666666654,
        16.877496666666595, 69.400986666666896, 114.45638666666677,
        209.43005666666741, 200.1995500000003, 256.93219000000016,
        169.85058999999947, 101.73759999999987, 89.123856666666683,
        110.00638666666649, 112.1381866666665, 76.28254666666659,
        25.317216666666742, 14.773776666666674, 15.909746666666461,
        16.524069999999799, 16.677776666666482, 23.464336666666547,
        143.21137666666618, 125.04142666666633, 132.06286666666625,
        286.17515000000009, 486.47381666666695, 522.56022666666672,
        270.07894666666687, 203.16550666666669, 170.04117666666656,
        169.5868399999998, 156.34694666666627, 257.88654999999915,
        235.10946666666618, 155.32937666666697, 69.812346666666443,
        81.089240000000061, 44.839640000000003, 41.413789999999899,
        27.790776666666694, 28.933306666666716, 89.048296666666545,
        89.588056666666404, 104.6396566666665, 91.88738999999994,
        41.81522999999985, 16.297709999999775, 26.643106666666387,
        28.781239999999684, 33.725989999999712, 29.152176666666513,
        27.378506666666436, 2.1810166666666069, 1.7737866666666289,
        11.894786666666516, 18.209120000000013, 18.342306666666666,
        26.322426666666889, 33.444536666666963, 27.83998666666697,
        44.781426666667102, 68.374346666667151, 77.597066666667047,
        53.473456666666891, 25.222039999999829, 25.71677666666654,
        24.262056666666659, 32.33524000000002, 43.476176666666703,
        67.690496666666633, 78.636229999999813, 55.721146666666542,
        69.893346666666659, 64.295069999999996, 69.558510000000041,
        44.029906666666633, 7.2864400000000655, 4.2359366666667562,
        4.2931366666667561, 4.4009766666668115, 4.95260000000013,
        9.2970966666667092, 16.816266666666714, 18.94367999999977,
        11.66486999999983, 11.924106666666582, 8.577639999999926,
        7.0129899999999425, 7.1201366666665988, 7.3069099999999167,
        1.6158966666666665, 1.3426800000000187, 18.054946666666712,
        22.744440000000075, 19.555470000000025, 14.061869999999947,
        25.854479999999789, 181.02401666666643, 320.05073666666635,
        399.24786666666716, 352.78546666666762, 168.84268000000048,
        15.915550000000204, 6.2970700000000672, 4.8646966666666964,
        6.2219466666666374, 71.169576666666671, 96.261870000000343,
        138.46836000000033, 111.51507000000011, 85.4710666666668,
        45.729826666666611, 112.95726999999999, 117.08014666666676,
        129.85875000000016, 69.311550000000224]

        self.sv_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, 49.294441071428437, 17.117771428571491,
        10.316857142857193, 7.792200000000113, 11.914342857142925,
        8.6909928571428683, 11.048857142857141, 12.870241071428543,
        50.265535714285875, 93.335726785714328, 215.71386964285756,
        262.30753571428602, 330.05868392857155, 319.13707857142828,
        246.00568571428565, 138.51982678571406, 107.23752678571421,
        80.45316428571418, 80.937599999999875, 88.727335714285545,
        61.682399999999852, 24.658885714285692, 19.863999999999926,
        14.441392857142663, 17.3969124999999, 112.88684107142822,
        116.16617142857106, 107.50734107142816, 214.30482857142857,
        350.21042678571445, 395.94720000000012, 394.49760000000009,
        380.62966964285704, 205.64795535714296, 167.94865714285729,
        156.18396964285694, 209.5319071428566, 231.39068392857092,
        289.05967857142821, 270.03731249999953, 215.33025000000018,
        94.408821428571301, 58.431812500000028, 34.166285714285742,
        31.902326785714227, 67.934735714285551, 112.90348571428542,
        136.71366964285681, 88.349914285714007, 77.893826785714154,
        67.273983928571326, 43.927683928571192, 21.405021428571199,
        25.359069642856916, 26.570799999999824, 30.23247857142843,
        23.76846964285706, 19.730507142856982, 9.4679839285712806,
        15.122126785714231, 15.303878571428543, 26.756169642857305,
        36.207869642857425, 29.213771428571732, 36.639571428571728,
        53.743098214286029, 60.81790714285745, 57.380942857143125,
        81.075255357143035, 74.449655357142873, 29.718942857142697,
        26.813826785714223, 32.070469642857162, 51.559969642857098,
        66.78751428571411, 65.538685714285549, 63.684535714285673,
        60.882741071428541, 65.283955357142887, 53.791612500000042,
        52.300512499999975, 34.171000000000006, 5.6966500000000764,
        5.3966500000001032, 6.7692839285715518, 8.1167839285715129,
        13.614942857142864, 23.996657142857043, 22.338612499999979,
        19.333312499999895, 16.33828571428554, 15.423998214285637,
        10.816241071428578, 6.8718785714285371, 5.4671357142856669,
        5.4469124999999279, 13.158055357142871, 19.0791982142858,
        20.911935714285818, 18.949142857142864, 29.646455357142763,
        169.60146964285676, 287.23776964285656, 358.25376964285715,
        408.03687857142876, 382.10099285714358, 306.49175535714386,
        141.92276964285753, 16.110314285714448, 9.1944285714285918,
        57.123821428571389, 91.034241071428724, 135.40754107142862,
        133.25160000000014, 144.40284107142864, 151.72948392857148,
        183.46585000000033, 133.01995535714272, 151.88114107142852,
        121.69107857142873]

        self.sv_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, 42.068272222222127, 17.244272222222239,
        15.941737777777767, 10.893001111111213, 12.510911111111206,
        11.09649444444446, 41.453026666666837, 79.423476666666744,
        178.27414333333368, 239.71152111111132, 363.66951222222207,
        416.32383222222199, 351.49306666666666, 260.29628888888874,
        197.89449888888888, 111.77924888888865, 83.824912222222167,
        69.35871111111102, 73.590173333333112, 74.342423333333102,
        53.790112222222021, 21.500684444444389, 22.567244444444434,
        95.07968444444414, 92.134404444444215, 92.196734444444147,
        173.93143999999995, 277.94833333333344, 316.48035666666669,
        309.71502666666663, 310.02600999999999, 308.99257888888883,
        333.45744999999999, 214.06417888888893, 207.59920444444418,
        193.70582222222188, 232.81434333333311, 289.61446222222173,
        375.99820999999952, 293.83004999999957, 176.41278777777788,
        77.954671111111068, 47.850534444444492, 57.52285444444432,
        89.480738888888652, 117.69128444444408, 122.66460555555523,
        116.65848999999974, 71.857599999999749, 76.929738888888721,
        72.446822222222053, 43.064115555555347, 20.952404444444305,
        23.753173333333212, 23.858893333333228, 24.419533333333245,
        22.154543333333212, 23.500916666666519, 13.258356666666595,
        23.675106666666736, 34.009716666666883, 30.965494444444701,
        34.637360000000257, 44.051272222222494, 50.554715555555745,
        51.654672222222388, 69.664894444444585, 82.330426666666739,
        82.575121111111173, 69.55284555555555, 34.978862222222105,
        41.221173333333283, 52.793795555555441, 52.157066666666537,
        56.7217566666666, 60.196449999999913, 58.500254444444444,
        51.280343333333356, 52.401587777777763, 48.082601111111188,
        44.470787777777801, 27.08958777777779, 6.9680177777778862,
        9.6670888888889603, 15.915894444444481, 21.768484444444407,
        20.469654444444391, 26.630267777777782, 29.029004444444393,
        24.743915555555443, 19.994005555555461, 15.796515555555503,
        9.1025955555555651, 5.5175999999999572, 12.355933333333295,
        16.436488888888917, 17.378445555555622, 18.340054444444455,
        32.585533333333316, 158.27235999999976, 268.86590666666626,
        363.49307666666647, 415.00397333333314, 397.64349000000027,
        408.22021000000046, 359.00707222222286, 270.92758222222301,
        127.56966666666696, 64.425476666666768, 86.301272222222394,
        124.1737822222222, 140.98406222222224, 160.90093333333323,
        190.36593333333346, 258.02618333333362, 252.72873777777775,
        237.07295111111137, 154.98595666666662]

    def test_standard_variance_period_6(self):
        period = 6
        sv = standard_variance.standard_variance(self.data, period)
        np.testing.assert_array_equal(sv, self.sv_period_6_expected)

    def test_standard_variance_period_8(self):
        period = 8
        sv = standard_variance.standard_variance(self.data, period)
        np.testing.assert_array_equal(sv, self.sv_period_8_expected)

    def test_standard_variance_period_10(self):
        period = 10
        sv = standard_variance.standard_variance(self.data, period)
        np.testing.assert_array_equal(sv, self.sv_period_10_expected)

    def test_standard_variance_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            standard_variance.standard_variance(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
