import unittest

import TestComputer
import TestBoard
import TestDatabaseHandler
import TestDice
import TestGame
import TestHuman
import TestPlayer
import TestQuestionHandler
import TestSettingsHandler

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(TestComputer))
suite.addTests(loader.loadTestsFromModule(TestBoard))
suite.addTests(loader.loadTestsFromModule(TestDatabaseHandler))
suite.addTests(loader.loadTestsFromModule(TestDice))
suite.addTests(loader.loadTestsFromModule(TestGame))
suite.addTests(loader.loadTestsFromModule(TestHuman))
suite.addTests(loader.loadTestsFromModule(TestPlayer))
suite.addTests(loader.loadTestsFromModule(TestQuestionHandler))
suite.addTests(loader.loadTestsFromModule(TestSettingsHandler))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
