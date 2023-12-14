Add-Type -AssemblyName System.Windows.Forms

while ($true) {
    $position = [System.Windows.Forms.Cursor]::Position

    Write-Host -NoNewline ("`rX: {0} | Y: {1}" -f $position.X, $position.Y)

    # Sleep for a short interval (e.g., 1 second)
    Start-Sleep -Seconds 1
}
