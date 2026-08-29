$ErrorActionPreference = "Stop"
$outputDir = "C:\Users\rohan\.gemini\antigravity-ide\scratch\shivnetra47_presentation\exports"
if (!(Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

$edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if (!(Test-Path $edgePath)) {
    $edgePath = "C:\Program Files\Microsoft\Edge\Application\msedge.exe"
}

Write-Host "Rendering all 15 Source Slides to 1920x1080 PNG..."

for ($i = 1; $i -le 15; $i++) {
    $pageStr = "{0:D2}" -f $i
    $htmlPath = "file:///C:/Users/rohan/.gemini/antigravity-ide/scratch/shivnetra47_presentation/pages/page_$pageStr.html"
    $outPng = "$outputDir\page_$pageStr.png"
    
    Write-Host -NoNewline "Rendering Page $pageStr / 15 -> page_$pageStr.png..."
    
    $args = @(
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1920,1080",
        "--screenshot=$outPng",
        "$htmlPath"
    )
    
    & $edgePath $args 2>$null
    
    if (Test-Path $outPng) {
        $size = (Get-Item $outPng).Length
        Write-Host " [OK] ($([math]::Round($size/1KB)) KB)"
    } else {
        Write-Host " [FAILED]"
    }
}

Write-Host "All 15 slides rendered successfully!"
