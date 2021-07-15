import unittest
import main as ootemplate

connexion = ootemplate.Connexion("localhost", "2002")


class Text(unittest.TestCase):

    def test_noformat(self):
        self.assertEqual({"gjerg": None, "jean": None, "aerhh": None, "rh": None, "aet": None, "h": None},
                         ootemplate.Template("unittest/files/text_vars_noformat.odt", connexion, False).scan())

    def test_format(self):
        self.assertEqual({"gjerg": None, "jean": None, "aerhh": None, "rh": None, "aet": None, "h": None},
                         ootemplate.Template("unittest/files/text_vars.odt", connexion, False).scan())

    def test_static_table(self):
        self.assertEqual({"var1": None, "var2": None},
                         ootemplate.Template("unittest/files/static_tab.odt", connexion, False).scan())


class Images(unittest.TestCase):

    def test(self):
        self.assertEqual({"image": {"path": None}},
                         ootemplate.Template("unittest/files/img_vars.odt", connexion, False).scan())


class Tables(unittest.TestCase):

    def test_multiple_row(self):
        self.assertEqual({"tab": [{"var1": None, "var2": None}]},
                         ootemplate.Template("unittest/files/multiple_row_tab.odt", connexion, False).scan())

    def test_one_row_varied(self):
        self.assertEqual({"tab": [{"var": None}]},
                         ootemplate.Template("unittest/files/one_row_tab_varied.odt", connexion, False).scan())

    def test_two_row_varied(self):
        self.assertEqual({"tab": [{"var1": None}]},
                         ootemplate.Template("unittest/files/two_row_tab_varied.odt", connexion, False).scan())

    def test_invalid_var(self):
        with self.assertRaises(ootemplate.TemplateVariableNotInLastRow):
            ootemplate.Template("unittest/files/invalid_var_tab.odt", connexion, False).scan()

    def test_invalid_vars(self):
        with self.assertRaises(ootemplate.TemplateVariableNotInLastRow):
            ootemplate.Template("unittest/files/invalid_vars_tab.odt", connexion, False).scan()

    def test_two_tabs_varied(self):
        self.assertEqual({"tab": [{"var1": None}], "tab2": [{"1": None, "2": None, "3": None, "4": None, "5": None}]},
                         ootemplate.Template("unittest/files/two_tabs_varied.odt", connexion, False).scan())


if __name__ == '__main__':
    unittest.main()
