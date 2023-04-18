pytest -s -v --capture=sys --html=Reports/report1.html --self-contained-html testCases/ --browser chrome
pytest -s -v --capture=sys --html=Reports/report2.html --self-contained-html testCases/ --browser firefox
pytest -s -v --capture=sys --html=Reports/report3.html --self-contained-html testCases/ --browser edge

@REM pytest -s -v -m "sanity" --capture=sys --html=Reports/report1.html --self-contained-html testCases/ --browser chrome
@REM pytest -s -v -m "sanity" --capture=sys --html=Reports/report2.html --self-contained-html testCases/ --browser firefox
@REM pytest -s -v -m "sanity" --capture=sys --html=Reports/report3.html --self-contained-html testCases/ --browser edge

@REM pytest -s -v -m "sanity or regression" --capture=sys --html=Reports/report1.html --self-contained-html testCases/ --browser chrome
@REM pytest -s -v -m "sanity and regression" --capture=sys --html=Reports/report1.html --self-contained-html testCases/ --browser chrome
@REM pytest -s -v -m "regression" --capture=sys --html=Reports/report1.html --self-contained-html testCases/ --browser chrome


@REM pytest -s -v -m "sanity or regression" --capture=sys --html=Reports/report1.html --self-contained-html testCases/ --browser firefox
@REM pytest -s -v -m "sanity and regression" --capture=sys --html=Reports/report1.html --self-contained-html testCases/ --browser firefox
@REM pytest -s -v -m "regression" --capture=sys --html=Reports/report1.html --self-contained-html testCases/ --browser firefox