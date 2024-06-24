import unittest
import pandas as pd
from data_handling import read_csv, clean_csv, rename_col
from data_processing import breakdown_date,erase_month


# Clase para hacer el setup que se use en todas las pruebas
class BaseSetupforTest(unittest.TestCase):

    def setUp(self):
        # Path to the test file
        self.file_path = 'Data/nics-firearm-background-checks.csv'

        # Llamada a la función de carga
        self.df = read_csv(self.file_path)

        # Clean the DataFrame
        self.df_clean = clean_csv(self.df)

        # Rename columns in the DataFrame
        self.df_renamed = rename_col(self.df_clean)

        # Separo la columna fecha en year y month
        self.df_divided = breakdown_date(self.df_renamed)

        # Borro la columna month
        self.df_removed = erase_month(self.df_divided)


# Pruebo la carga de datos
class SetupforDataHandling(BaseSetupforTest):

    def test_read_csv(self):
        # Load the file using the function
        df_result = read_csv(self.file_path)

        # Check if the loaded DataFrame matches the expected DataFrame
        pd.testing.assert_frame_equal(df_result, self.df)


# Pruebo las columnas tras la limpieza de datos
class SetupforTestCleanCSV(BaseSetupforTest):

    def test_clean_csv(self):
        # Expected columns after cleaning
        expected_columns = ['month', 'state', 'permit', 'handgun', 'long_gun']

        # Check if the columns match
        actual_columns = list(self.df_clean.columns)
        self.assertEqual(actual_columns, expected_columns)


# Pruebo que se han renombrado correctamete
class SetupforTestRenameCol(BaseSetupforTest):

    def test_rename_col(self):
        # Expected columns after renaming
        expected_columns = ['state', 'permit', 'handgun', 'longgun', 'year']

        # Check if the columns match
        actual_columns = list(self.df_renamed.columns)
        self.assertEqual(actual_columns, expected_columns)


#Pruebo la division por estado
class SetupforDataProcessing(BaseSetupforTest):

    def test_breakdown_date(self):
        # Aplicar la función breakdown_date
        df_result = breakdown_date(self.df_clean)

        # Verificar la estructura del DataFrame resultante
        self.assertIn('year', df_result.columns)
        self.assertIn('month', df_result.columns)

    def test_erase_month(self):
        # Llamar a la funcion de eliminar mes
        print('NUEVA')
        df_result = erase_month(self.df_clean)
        print(df_result.head(5))

        # Verificar que la columna 'month' no existe
        self.assertNotIn('month', df_result.columns)

if __name__ == "__main__":
    unittest.main()
