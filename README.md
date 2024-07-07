# KinD
Kinematic Video Detector Web Crawler "Be KinD, Please Rewind"

TAILORED FROM https://github.com/hank-ai/darknet/blob/master/README.md#windows-cmake-method

In PowerShell (Admin)

```
winget install Git.Git
winget install Kitware.CMake
winget install nsis.nsis
winget install Microsoft.VisualStudio.2022.Community
```

Open Visual Studio Installer and choose `Modify`
Check .NET desktop development
Check Desktop development with C++
Choose `Modify`


Run the following commands to install Microsoft VCPKG, which will then be used to build OpenCV:

```
cd c:\
mkdir c:\src
cd c:\src
git clone https://github.com/microsoft/vcpkg
cd vcpkg
bootstrap-vcpkg.bat
.\vcpkg.exe integrate install
.\vcpkg.exe integrate powershell
.\vcpkg.exe install opencv[contrib,dnn,freetype,jpeg,openmp,png,webp,world]:x64-windows pthreads:x64-windows


Once all of the previous steps have finished successfully, you need to clone Darknet and build it. During this step you also need to tell CMake where the vcpkg is located so it can find OpenCV and other dependencies:

```
cd c:\src
git clone https://github.com/hank-ai/darknet.git
cd darknet
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=C:/src/vcpkg/scripts/buildsystems/vcpkg.cmake ..
msbuild.exe "/property:Platform=x64;Configuration=Release" /target:Build -maxCpuCount -verbosity:normal -detailedSummary darknet.sln
```

Add msbuild.exe and darknet to PATH

```
setx PATH "%PATH%;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin"
setx PATH "%PATH%;C:\src\darknet\"
setx PATH "%PATH%;C:\src\darknet\build"
setx PATH "%PATH%;C:\src\darknet\build\release"
setx PATH "%path%;C:\opencv\build\x64\vc15\bin"
```

To properly package up the following:
• Darknet
• libraries
• include files
• DLLs

Create the NSIS installation package with this: 	

```
msbuild.exe "/property:Platform=x64;Configuration=Release" PACKAGE.vcxproj
```
