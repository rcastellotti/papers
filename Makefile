build: 
	python3 app.py
	cp -r papers/* build/
	cp -r static/Sans/ build/Sans
	cp -r static/Typewriter/ build/Typewriter
	cp static/pygments.css build/
	tailwindcss  -i ./static/input.css -o ./build/output.css --minify
clean:
	rm -rf build