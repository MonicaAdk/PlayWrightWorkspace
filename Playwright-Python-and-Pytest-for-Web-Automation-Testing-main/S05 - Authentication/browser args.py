browser = playwright.chromium.launch(
	#...
	args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"]
)