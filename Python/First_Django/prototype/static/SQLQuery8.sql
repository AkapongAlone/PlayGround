USE [master]
GO
/****** Object:  Database [Longdo]    Script Date: 2/8/2564 13:45:19 ******/
CREATE DATABASE [Longdo]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Longdo', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\Longdo.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Longdo_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\Longdo_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [Longdo] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Longdo].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Longdo] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Longdo] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Longdo] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Longdo] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Longdo] SET ARITHABORT OFF 
GO
ALTER DATABASE [Longdo] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [Longdo] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Longdo] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Longdo] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Longdo] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Longdo] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Longdo] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Longdo] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Longdo] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Longdo] SET  ENABLE_BROKER 
GO
ALTER DATABASE [Longdo] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Longdo] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Longdo] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Longdo] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Longdo] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Longdo] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Longdo] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Longdo] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [Longdo] SET  MULTI_USER 
GO
ALTER DATABASE [Longdo] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Longdo] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Longdo] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Longdo] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Longdo] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Longdo] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [Longdo] SET QUERY_STORE = OFF
GO
USE [Longdo]
GO
/****** Object:  Table [dbo].[Collect_data]    Script Date: 2/8/2564 13:45:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Collect_data](
	[cid] [int] IDENTITY(1,1) NOT NULL,
	[wid] [int] NULL,
	[Duration] [nvarchar](50) NULL,
	[Result] [nvarchar](50) NULL,
	[Point] [nchar](10) NULL,
	[Number] [int] NULL,
 CONSTRAINT [PK_Collect_data] PRIMARY KEY CLUSTERED 
(
	[cid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Items]    Script Date: 2/8/2564 13:45:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Items](
	[iid] [int] IDENTITY(1,1) NOT NULL,
	[item] [char](10) NULL,
	[pid] [int] NULL,
 CONSTRAINT [PK_Items] PRIMARY KEY CLUSTERED 
(
	[iid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Model]    Script Date: 2/8/2564 13:45:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Model](
	[wid] [int] IDENTITY(1,1) NOT NULL,
	[Model] [nvarchar](50) NULL,
	[tid] [int] NULL,
	[Tooltype] [nvarchar](50) NULL,
	[Cstart] [int] NULL,
	[Rstart] [int] NULL,
	[Excel] [nvarchar](max) NULL,
	[img] [nvarchar](max) NULL,
	[Point] [nvarchar](max) NULL,
	[Toolname] [nvarchar](max) NULL,
 CONSTRAINT [PK_Model] PRIMARY KEY CLUSTERED 
(
	[wid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Produc]    Script Date: 2/8/2564 13:45:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Produc](
	[pid] [int] IDENTITY(1,1) NOT NULL,
	[product] [char](10) NULL,
 CONSTRAINT [PK_Produc] PRIMARY KEY CLUSTERED 
(
	[pid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Time]    Script Date: 2/8/2564 13:45:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Time](
	[tid] [int] IDENTITY(1,1) NOT NULL,
	[Timein] [time](7) NULL,
	[Timeout] [time](7) NULL,
	[Duration] [nvarchar](50) NULL,
	[Date] [date] NULL,
	[wid] [int] NULL,
	[Number] [int] NULL,
 CONSTRAINT [PK_Time] PRIMARY KEY CLUSTERED 
(
	[tid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Tool_]    Script Date: 2/8/2564 13:45:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Tool_](
	[tid] [int] IDENTITY(1,1) NOT NULL,
	[CodeName] [nvarchar](50) NULL,
 CONSTRAINT [PK_Tool_] PRIMARY KEY CLUSTERED 
(
	[tid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Work]    Script Date: 2/8/2564 13:45:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Work](
	[rid] [int] IDENTITY(1,1) NOT NULL,
	[Man] [nvarchar](50) NULL,
	[Timein] [time](7) NULL,
	[Timeout] [time](7) NULL,
	[Duration] [nvarchar](50) NULL,
	[Date] [date] NULL,
	[wid] [int] NULL,
	[Result] [nvarchar](max) NULL,
	[Number] [int] NULL,
 CONSTRAINT [PK_Work] PRIMARY KEY CLUSTERED 
(
	[rid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[Items]  WITH CHECK ADD  CONSTRAINT [FK_Items_Produc] FOREIGN KEY([pid])
REFERENCES [dbo].[Produc] ([pid])
GO
ALTER TABLE [dbo].[Items] CHECK CONSTRAINT [FK_Items_Produc]
GO
ALTER TABLE [dbo].[Model]  WITH CHECK ADD  CONSTRAINT [FK_Model_Tool_1] FOREIGN KEY([tid])
REFERENCES [dbo].[Tool_] ([tid])
GO
ALTER TABLE [dbo].[Model] CHECK CONSTRAINT [FK_Model_Tool_1]
GO
ALTER TABLE [dbo].[Work]  WITH CHECK ADD  CONSTRAINT [FK_Work_Model] FOREIGN KEY([wid])
REFERENCES [dbo].[Model] ([wid])
GO
ALTER TABLE [dbo].[Work] CHECK CONSTRAINT [FK_Work_Model]
GO
USE [master]
GO
ALTER DATABASE [Longdo] SET  READ_WRITE 
GO
