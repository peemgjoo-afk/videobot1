name: Build APK
on: [push]

jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Set up Java 11
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '11'

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install buildozer==1.5.0
          pip install Cython==3.0.11
          sudo apt-get update -qq
          sudo apt-get install -y unzip

      - name: Build APK
        run: |
          mkdir -p $HOME/.buildozer/android/platform/android-sdk/cmdline-tools
          cd $HOME/.buildozer/android/platform/android-sdk/cmdline-tools
          wget -q https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O cmdline-tools.zip
          unzip -q cmdline-tools.zip
          mkdir -p latest
          mv cmdline-tools/* latest/ || true
          mv lib latest/ 2>/dev/null || true
          mkdir -p licenses
          echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > licenses/android-sdk-license
          echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> licenses/android-sdk-license
          echo "24333f8a63b6825ea9c5514f83c1059b8ea731b" > licenses/android-sdk-preview-license
          cd $GITHUB_WORKSPACE
          buildozer -v android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: apk
          path: bin/*.apk
