default:
	@cat makefile

get_texts:
	wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt
	wget https://www.gutenberg.org/cache/epub/932/pg932.txt
	wget https://www.gutenberg.org/cache/epub/1064/pg1064.txt
	wget https://www.gutenberg.org/cache/epub/51060/pg51060.txt
	wget https://www.gutenberg.org/cache/epub/32037/pg32037.txt
	wget https://www.gutenberg.org/cache/epub/50852/pg50852.txt
	wget https://www.gutenberg.org/cache/epub/8893/pg8893.txt
	wget https://www.gutenberg.org/cache/epub/55175/pg55175.txt
	wget https://www.gutenberg.org/cache/epub/37397/pg37397.txt
	wget https://www.gutenberg.org/cache/epub/48383/pg48383.txt

raven_line_count:
	cat pg17192.txt | wc -l

raven_word_count:
	cat pg17192.txt | wc -w

raven_counts:
	cat pg17192.txt | grep raven | wc -l
	cat pg17192.txt | grep Raven | wc -l
	cat pg17192.txt | grep -i raven | wc -l

total_lines:
	cat pg*.txt | wc -l 

total_words:
	cat pg*.txt | wc -w

install_requirements:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip; pip install -r requirements.txt

test:
	pytest -vvx tests/
