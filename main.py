from lexer import lg
from sql import SqlFileReader
from parsing import SyntaxAnalyzer

sql_file = SqlFileReader('sql.sql')


lex = lg.build()
identified_tokens = lex.lex(sql_file.one_line)


synax = SyntaxAnalyzer(sql_file, identified_tokens)

synax.start_analysis()


if __name__ == '__main__':
    pass
