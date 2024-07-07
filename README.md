# KinD
Kinematic Video Detector Web Crawler "Be KinD, Please Rewind"

TAILORED FROM https://github.com/hank-ai/darknet/blob/master/README.md#windows-cmake-method

FROM POWERSHELL ADMINISTRATOR
RUN EACH COMMAND LINE-BY-LINE

`winget install Git.Git` <br>
`winget install Kitware.CMake` <br>
`winget install nsis.nsis` <br>
`winget install Microsoft.VisualStudio.2022.Community` <br>


Open Visual Studio Installer and choose `Modify`
Check .NET desktop development
Check Desktop development with C++
Choose `Modify`


Run the following commands to install Microsoft VCPKG, which will then be used to build OpenCV:

`cd c:\` <br>
`mkdir c:\src` <br>
`cd c:\src` <br>
`git clone https://github.com/microsoft/vcpkg` <br>
`cd vcpkg` <br>
`bootstrap-vcpkg.bat` <br>
`.\vcpkg.exe integrate install` <br>
`.\vcpkg.exe integrate powershell` <br>
`.\vcpkg.exe install opencv[contrib,dnn,freetype,jpeg,openmp,png,webp,world]:x64-windows pthreads:x64-windows` <br>


Once all of the previous steps have finished successfully, you need to clone Darknet and build it. During this step we also need to tell CMake where vcpkg is located so it can find OpenCV and other dependencies:

`cd c:\src` <br>
`git clone https://github.com/hank-ai/darknet.git` <br>
`cd darknet` <br>
`mkdir build` <br>
`cd build` <br>
`cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=C:/src/vcpkg/scripts/buildsystems/vcpkg.cmake ..` <br>
`msbuild.exe "/property:Platform=x64;Configuration=Release" /target:Build -maxCpuCount -verbosity:normal -detailedSummary darknet.sln` <br>


FROM ADMINISTRATOR: DEVELOPER POWERSHELL FOR VS 2022 Add msbuild.exe and darknet to PATH

`setx PATH "%PATH%;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin"` <br>
`setx PATH "%PATH%;C:\src\darknet\"` <br>
`setx PATH "%PATH%;C:\src\darknet\build"` <br>
`setx PATH "%PATH%;C:\src\darknet\build\release"` <br>
`setx PATH "%path%;C:\opencv\build\x64\vc15\bin"` <br>


To properly package up Darknet, the libraries, the include files, and the necessary DLLs, create the NSIS installation package like this: 	

`msbuild.exe "/property:Platform=x64;Configuration=Release" PACKAGE.vcxproj` <br>
